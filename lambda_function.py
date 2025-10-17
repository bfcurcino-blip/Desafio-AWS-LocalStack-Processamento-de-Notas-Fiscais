import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
    table = dynamodb.Table('NotasFiscais')

    for record in event['Records']:
        body = json.loads(record['body']) if 'body' in record else {}
        id_nf = body.get('id', 'NF-desconhecida')
        cliente = body.get('cliente', 'Desconhecido')
        valor = body.get('valor', 0)
        data_emissao = body.get('data_emissao', 'N/A')

        table.put_item(Item={
            'id': id_nf,
            'cliente': cliente,
            'valor': valor,
            'data_emissao': data_emissao
        })

    return {
        'statusCode': 200,
        'body': json.dumps('Nota fiscal gravada com sucesso!')
    }
