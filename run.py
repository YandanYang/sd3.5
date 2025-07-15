import sd3_infer

prompt = "A 176*39*45cm tv_stand with vase and remote control on the top."

out_dir = sd3_infer.main(prompt=prompt) 
print(out_dir)