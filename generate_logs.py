import click, time, datetime, random, requests

states = ["Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming",
"District of Columbia",
"Puerto Rico",
"Guam",
"American Samoa",
"U.S. Virgin Islands",
"Northern Mariana Islands"]

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
def generate_logs(count):
    """Generate {count} logs."""
    
    for x in range(count):
        
        dt = datetime.datetime.now().date().strftime("%m-%d-%Y")
        tm = time.strftime("%H:%M:%S")
        status = random.choice(["up", "up", "up", "up", "up", "up", "up", "up", "up", "down"])
        state = random.choice(states)

        date_time = "{} {}" . format (dt, tm)
    	message = "{} - {}: {}" . format (date_time, status, state)
    	
    	data = {
    		"date_time": date_time,
    		"date": dt,
    		"time": tm,
    		"status": status,
    		"state": state
    	}

    	response = requests.post("http://104.236.214.67:8201/incoming/statusdata", json=data)
    	print(response.content)

    	"""
    	with open("logstash/inputs/events.log", "a") as log_file:
    		log_file.write("{}\n" . format(message))
    		wait_period = random.choice(range(0,10))
    		print(".")
    		time.sleep(wait_period)
    	"""

if __name__ == '__main__':
    generate_logs()


