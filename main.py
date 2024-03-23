from PIL import Image
import requests
from transformers import (BlipProcessor, BlipForConditionalGeneration, 
                          AutoTokenizer, AutoModelForSeq2SeqLM)
import pickle

blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_desc(img_url, text, url):
    if url:
        raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')
    else:
        raw_image = Image.open(img_url).convert('RGB')
    
    if text:
        # conditional image captioning
        inputs = blip_processor(raw_image, text, return_tensors="pt")
        out = blip_model.generate(**inputs)
        return blip_processor.decode(out[0], skip_special_tokens=True)
    else:
        # unconditional image captioning
        inputs = blip_processor(raw_image, return_tensors="pt")
        out = blip_model.generate(**inputs)
        return blip_processor.decode(out[0], skip_special_tokens=True)
    

t5_tokenizer = AutoTokenizer.from_pretrained('prasanthsagirala/text-to-social-media-captions')
t5_model = AutoModelForSeq2SeqLM.from_pretrained('prasanthsagirala/text-to-social-media-captions')

def generate_caption(text="a woman playing soccer"):
    inputs = ["captionize: " + text]
    inputs = t5_tokenizer(inputs, max_length=512, truncation=True, return_tensors="pt")
    output = t5_model.generate(**inputs, num_beams=8, do_sample=True, min_length=10, max_length=64)
    decoded_output = t5_tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    return decoded_output

def generate_caption_for_img(img_link='https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg', text="", url=False, img_show=True):
    img_desc = generate_desc(img_link, text, url)
    if img_show:
        if url:
            Image.open(requests.get(img_link, stream=True).raw).show()
        else:
            Image.open(img_link).show()

    print('Image Description:', img_desc)
    caption = generate_caption(img_desc)
    print('Caption:', caption)

# Create a dictionary to store all functions and models
pickle_data = {
    'generate_desc': generate_desc,
    'generate_caption': generate_caption,
    'generate_caption_for_img': generate_caption_for_img,
    'blip_processor': blip_processor,
    'blip_model': blip_model,
    't5_tokenizer': t5_tokenizer,
    't5_model': t5_model
}

# Pickle the dictionary
with open('image_captioning.pkl', 'wb') as f:
    pickle.dump(pickle_data, f)

# Test the pickled functions
generate_caption_for_img(url=True)
img_link = "temp.png"
generate_caption_for_img(img_link)
