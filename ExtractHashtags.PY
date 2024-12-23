import re

def extract_hashtags(text):
    
    return re.findall(r"#\w+", text)

def main():
    
    file_path = "tweets.txt" 
    with open(file_path, "r") as file:
            all_hashtags = []
            for line in file:
                all_hashtags.extend(extract_hashtags(line.strip()))
            
            
            print("Hashtags extraits :")
            for hashtag in all_hashtags:
                print(hashtag)


if __name__ == "__main__":
    main()
