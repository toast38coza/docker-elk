import click, time, datetime, random


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
def generate_logs(count):
    """Generate {count} logs."""
    
    for x in range(count):
        
        dt = datetime.datetime.now().date().strftime("%m-%d-%Y")
        tm = time.strftime("%H:%M:%S")
        status = random.choice(["up", "up", "up", "up", "up", "up", "up", "up", "up", "down"])
        province = random.choice(["The Eastern Cape", "The Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "The Northern Cape", "North West"])

        date_time = "{} {}" . format (dt, tm)
    	message = "{} - {}: {}" . format (date_time, status, province)
    	
    	with open("log/events.log", "a") as log_file:
    		log_file.write("{}\n" . format(message))
    		wait_period = random.choice(range(0,10))
    		print(".")
    		time.sleep(wait_period)


if __name__ == '__main__':
    generate_logs()