import os
import re

STARTING_FOLDER = 'yelp_reviews_nyc'
DESTINATION_FOLDER = 'reviews_no_attribution'

def extract_review_text():
    files = os.listdir(STARTING_FOLDER)
    files_full_path = [STARTING_FOLDER + f'/{filename}' for filename in files]
    for file in files_full_path:
        extract_text_only(file)

def extract_text_only(file):
    reviews = []
    for line in open(file):
        match = re.search('#REVIEW#(.+)', line)
        if (match):
            reviews.append(match.group(1))
    with open(DESTINATION_FOLDER + '/lines.txt', 'a+') as writer:
        writer.write('\n'.join(reviews))


if __name__ == "__main__":
    extract_review_text()
