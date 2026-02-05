import os

DATASET_DIR = "./datasets"
DICT_PATH = "./dictionary/custom.dict"
ACOUSTIC_MODEL = "english_us_arpa"
OUTPUT_DIR = "./aligned_output_fixed"

cmd = f"mfa align {DATASET_DIR} {DICT_PATH} {ACOUSTIC_MODEL} {OUTPUT_DIR} --clean"
print("Running:", cmd)
os.system(cmd)
