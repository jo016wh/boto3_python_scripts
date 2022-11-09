import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(TargetLanguageCode='fr',Text='I am learning to code in AWS',SourceLanguageCode='en')

if __name__=="__main__":
    main()

