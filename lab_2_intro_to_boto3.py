
import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

translate_text() # This line will call our function. Without it, python will not do anything.

# terminal output: {'TranslatedText': "J'apprends à coder dans AWS", 'SourceLanguageCode': 'en', 'TargetLanguageCode': 'fr', 'ResponseMetadata': {'RequestId': 'db2e2966-000a-4474-97cd-337b6249b783', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'db2e2966-000a-4474-97cd-337b6249b783', 'cache-control': 'no-cache', 'content-type': 'application/x-amz-json-1.1', 'content-length': '101', 'date': 'Fri, 28 Feb 2020 10:14:32 GMT'}, 'RetryAttempts': 0}}

Return type
    dict

Returns
    Response Syntax

    {
        'TranslatedText': 'string',
        'SourceLanguageCode': 'string',
        'TargetLanguageCode': 'string',
        'AppliedTerminologies': [
            {
                'Name': 'string',
                'Terms': [
                    {
                        'SourceText': 'string',
                        'TargetText': 'string'
                    },
                ]
            },
        ]
    }

