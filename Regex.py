import re

def validate_email(email):
   

    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    if re.match(email_pattern, email) :
        return True
    else:
        return False 
    
def  valnuméro():
    numéro_pattern =r'([0](6|7|5)([0-9]{8}))|((\\+213 )(6|7|5)([0-9]{8}))'
    if re.match(numéro_pattern, numéro):
       return True
    else:
        return False 

def extract_hashtags(text):
    return re.findall(r"#\w+", text)


    
if __name__ == "__main__":
    email = input("Enter an email address to validate: ")
    if validate_email(email):
        print(f"The email address {email} is valid.")
    else:
        print(f"The email address {email} is invalid.")
    numéro = input("Enter an numéro to validate: ")
    if validate_email( numéro):
        print(f"The numéro{ numéro} is valid.")
    else:
        print(f"The numéro { numéro} is invalid.")
        
      
    file_path = "tweets.txt" 
    with open(file_path, "r") as file:
            all_hashtags = []
            for line in file:
                all_hashtags.extend(extract_hashtags(line.strip()))
            

            print("Hashtags extraits :")
            for hashtag in all_hashtags:
                print(hashtag)
  