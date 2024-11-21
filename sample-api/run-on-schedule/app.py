from chalice import Chalice
import boto3 

app = Chalice(app_name='run-on-schedule')

instance_id = "id-3271893021"
ec2 = boto3.client('ec2')

@app.schedule('cron(0 0 * * *)')
def daily_task():
    print("Running daily task at midnight")
    response = ec2.start_instances(instance_id)

#@app.lambda_function()
#def first_function(event, context):
#    return {'hello': 'world'}


#@app.lambda_function()
#def second_function(event, context):
#    return {'hello': 'world2'}
