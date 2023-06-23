import re
import argparse

def load_file(path):
    with open(path) as f:
        plain_template = f.readlines()

    return plain_template


def process_plain_template(plain_template, key_words=("VARIETY", "PLOT", "ROOT", "POLL")):
    counter = {k: 0 for k in key_words}

    out = ""
    for line in plain_template:
        for k in key_words:
            if k in line:
                line = line.replace(k, f"{k}_{counter[k]}")
                counter[k] += 1

        out += f"{line}\n"

    return out

def main(in_path, out_path, key_words=("VARIETY", "PLOT", "ROOT", "POLL")):
    plain_template = load_file(in_path)
    processed_template = process_plain_template(plain_template, key_words)

    with open(out_path, "w") as f:
        f.write(processed_template)




