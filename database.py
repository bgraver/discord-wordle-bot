import boto3


# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('wordle')

'''
    Item={
    'username': item['username'],
    'day': item['day'],
    'score': item['score'],
    'blob': item['blob']
}
'''


# Querying the db for username
def put_scores(item):
    response = table.put_item(
        Item={
            'username': item['author'],
            'day': item['day'],
            'score': item['score'],
            'blob': item['blob']
        }
    )
    return response

'''
1) Only letting 
'''
# def leaderboard():






