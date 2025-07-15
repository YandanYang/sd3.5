# Stable Diffusion 3.5 for [SceneWeaver](https://github.com/YandanYang/SceneWeaver)

This repository is forked from [Stable Diffusion 3.5](https://github.com/Stability-AI/sd3.5).

## Download

Download the following models from HuggingFace into `models` directory:
1. [Stability AI SD3.5 Large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/sd3.5_large.safetensors) (default) or [Stability AI SD3.5 Large Turbo](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-turbo/blob/main/sd3.5_large_turbo.safetensors) or [Stability AI SD3.5 Medium](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium/blob/main/sd3.5_medium.safetensors)
2. [OpenAI CLIP-L](https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/text_encoders/clip_l.safetensors)
3. [OpenCLIP bigG](https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/text_encoders/clip_g.safetensors)
4. [Google T5-XXL](https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/text_encoders/t5xxl_fp16.safetensors)

## Install

```sh
# Note: on windows use "python" not "python3"
python3 -s -m venv .sd3.5
source .sd3.5/bin/activate
# or on windows: venv/scripts/activate
python3 -s -m pip install -r requirements.txt
```

## Config 

Modify the `prompt` and `img_savedir` in `prompt.json`:
```
{
    "prompt": "An entire 120cm * 60cm * 75cm desk fully visible on the ground, with a laptop, notebook, pen, and coffee mug on top of it. The entire desk, including the bottom and the objects on it, should be visible in the frame. The background is clean with nothing else nearby.",
    "img_savedir": "SD_img.jpg"
}
```
## Run

```sh
# Generate a cat using SD3.5 Large model (at models/sd3.5_large.safetensors) with its default settings
python3 sd3_infer_acdc.py 
```

Images will be output to `img_savedir` defined in `prompt.json`.


To change the resolution of the generated image, modify `WIDTH` and `HEIGHT` in `sd3_infer_acdc.py`.

To change the SD model, modify `MODEL` in `sd3_infer_acdc.py`.


## File Guide

- `sd3_infer_acdc.py` - entry point, review this for basic usage of diffusion model 
- `prompt.json` - contains the image generation prompt and output dir 
- `sd3_impls.py` - contains the wrapper around the MMDiTX and the VAE
- `other_impls.py` - contains the CLIP models, the T5 model, and some utilities
- `mmditx.py` - contains the core of the MMDiT-X itself
- folder `models` with the following files (download separately):
    - `clip_l.safetensors` (OpenAI CLIP-L, same as SDXL/SD3, can grab a public copy)
    - `clip_g.safetensors` (openclip bigG, same as SDXL/SD3, can grab a public copy)
    - `t5xxl.safetensors` (google T5-v1.1-XXL, can grab a public copy)
    - `sd3.5_large.safetensors` or `sd3.5_large_turbo.safetensors` or `sd3.5_medium.safetensors` (or `sd3_medium.safetensors`)


## Legal

Check the LICENSE-CODE file.

### Note

Some code in `other_impls` originates from HuggingFace and is subject to [the HuggingFace Transformers Apache2 License](https://github.com/huggingface/transformers/blob/main/LICENSE)
