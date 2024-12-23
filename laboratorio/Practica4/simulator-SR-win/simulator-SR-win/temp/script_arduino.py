import libraries.standard as standard
import libraries.serial as Serial
import libraries.string as String
import graphics.screen_updater as screen_updater
import libraries.servo as Servo


NO_LINEA = 0
LINEA = 1
TURN_AROUND_TIME = 1700
QUARTER_BACK_TIME = 400
EXTRA_FORWARD_TIME = 225
servoIzq = Servo.Servo(standard.board)
servoDer = Servo.Servo(standard.board)
pinIrIzqIzq = 10
pinIrIzq = 2
pinIrDer = 3
pinIrDerDer = 11
pinServoDer = 9
pinServoIzq = 8
irSensorValues = [0, 0, 0, 0]

seed = 12345
searching = False

def setup():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	Serial.begin(9600)
	standard.pin_mode(pinIrIzqIzq, 0)
	standard.pin_mode(pinIrDerDer, 0)
	standard.pin_mode(pinIrDer, 0)
	standard.pin_mode(pinIrIzq, 0)
	servoIzq.attach(pinServoIzq)
	servoDer.attach(pinServoDer)
	stopMotor()
	standard.delay(500)
	forward()

def loop():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	readIRSensor()
	if ((((irSensorValues[0] == NO_LINEA) and (irSensorValues[1] == LINEA)) and (irSensorValues[2] == LINEA)) and (irSensorValues[3] == NO_LINEA)):
		forwardMotor()
	elif ((((irSensorValues[0] == LINEA) and (irSensorValues[1] == LINEA)) and (irSensorValues[2] == LINEA)) and (irSensorValues[3] == LINEA)):
		forwardMotor1((EXTRA_FORWARD_TIME / 2))
	elif ((((irSensorValues[0] == LINEA) and (irSensorValues[1] == NO_LINEA)) and (irSensorValues[2] == NO_LINEA)) and (irSensorValues[3] == LINEA)):
		stopMotor()
	elif ((((irSensorValues[0] == NO_LINEA) and (irSensorValues[1] == NO_LINEA)) and (irSensorValues[2] == NO_LINEA)) and (irSensorValues[3] == NO_LINEA)):
		probabilisticSearch()
	elif ((((irSensorValues[0] == LINEA) and (irSensorValues[1] == NO_LINEA)) and (irSensorValues[2] == NO_LINEA)) and (irSensorValues[3] == LINEA)):
		turnLeft()
	elif ((((irSensorValues[0] == NO_LINEA) and (irSensorValues[1] == NO_LINEA)) and (irSensorValues[2] == NO_LINEA)) and (irSensorValues[3] == LINEA)):
		turnRight()
	elif ((((irSensorValues[0] == LINEA) and (irSensorValues[1] == LINEA)) and (irSensorValues[2] == NO_LINEA)) and (irSensorValues[3] == NO_LINEA)):
		turnLeft()
	elif ((((irSensorValues[0] == NO_LINEA) and (irSensorValues[1] == NO_LINEA)) and (irSensorValues[2] == LINEA)) and (irSensorValues[3] == LINEA)):
		turnRight()
	elif ((((irSensorValues[0] == LINEA) and (irSensorValues[1] == LINEA)) and (irSensorValues[2] == LINEA)) and (irSensorValues[3] == NO_LINEA)):
		turnLeft()
	elif ((((irSensorValues[0] == NO_LINEA) and (irSensorValues[1] == LINEA)) and (irSensorValues[2] == LINEA)) and (irSensorValues[3] == LINEA)):
		turnRight()
	elif ((((irSensorValues[0] == LINEA) and (irSensorValues[1] == NO_LINEA)) and (irSensorValues[2] == LINEA)) and (irSensorValues[3] == NO_LINEA)):
		forwardMotor()
	elif ((((irSensorValues[0] == NO_LINEA) and (irSensorValues[1] == LINEA)) and (irSensorValues[2] == NO_LINEA)) and (irSensorValues[3] == LINEA)):
		forwardMotor()
	elif ((((irSensorValues[0] == LINEA) and (irSensorValues[1] == NO_LINEA)) and (irSensorValues[2] == LINEA)) and (irSensorValues[3] == LINEA)):
		turnRight()
	elif ((((irSensorValues[0] == LINEA) and (irSensorValues[1] == LINEA)) and (irSensorValues[2] == NO_LINEA)) and (irSensorValues[3] == LINEA)):
		turnLeft()
	elif ((((irSensorValues[0] == NO_LINEA) and (irSensorValues[1] == LINEA)) and (irSensorValues[2] == NO_LINEA)) and (irSensorValues[3] == NO_LINEA)):
		turnLeft()
	elif ((((irSensorValues[0] == NO_LINEA) and (irSensorValues[1] == NO_LINEA)) and (irSensorValues[2] == LINEA)) and (irSensorValues[3] == NO_LINEA)):
		turnRight()
	if searching:
		probabilisticSearchStep()

def readIRSensor():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	irSensorValues[0] = standard.digital_read(pinIrIzqIzq)
	irSensorValues[1] = standard.digital_read(pinIrIzq)
	irSensorValues[2] = standard.digital_read(pinIrDer)
	irSensorValues[3] = standard.digital_read(pinIrDerDer)

def forward():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	if ((standard.digital_read(pinIrIzq) == NO_LINEA) and (standard.digital_read(pinIrDer) == LINEA)):
		servoIzq.write(0)
		servoDer.write(90)
	elif ((standard.digital_read(pinIrIzq) == LINEA) and (standard.digital_read(pinIrDer) == NO_LINEA)):
		servoIzq.write(90)
		servoDer.write(180)
	elif ((standard.digital_read(pinIrIzq) == LINEA) or (standard.digital_read(pinIrDer) == LINEA)):
		forwardMotor()
	elif ((standard.digital_read(pinIrIzq) == NO_LINEA) and (standard.digital_read(pinIrDer) == NO_LINEA)):
		stopMotor()

def stopMotor():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	servoIzq.write(90)
	servoDer.write(90)

def forwardMotor():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	servoIzq.write(0)
	servoDer.write(180)

def forwardMotor1(xTime = 0):
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	forwardMotor()
	standard.delay(xTime)

def turnAround():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	servoIzq.write(0)
	servoDer.write(0)
	standard.delay(QUARTER_BACK_TIME)
	forward()

def turnRight():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	forwardMotor1((EXTRA_FORWARD_TIME / 4))
	servoIzq.write(0)
	servoDer.write(0)
	standard.delay((QUARTER_BACK_TIME / 4))
	forward()

def turnLeft():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	forwardMotor1((EXTRA_FORWARD_TIME / 4))
	servoIzq.write(180)
	servoDer.write(180)
	standard.delay((QUARTER_BACK_TIME / 4))
	forward()

def probabilisticSearch():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	searching = True

def probabilisticSearchStep():
	global NO_LINEA
	global LINEA
	global TURN_AROUND_TIME
	global QUARTER_BACK_TIME
	global EXTRA_FORWARD_TIME
	global servoIzq
	global servoDer
	global pinIrIzqIzq
	global pinIrIzq
	global pinIrDer
	global pinIrDerDer
	global pinServoDer
	global pinServoIzq
	global irSensorValues
	global seed
	global searching
	bit = 0
	seed = (((1664525 * seed) + 1013904223) % 4294967296)
	Serial.println((String.String("El bit aleatorio es: ") + (seed & 1)))
	bit = (seed & 1)
	if (bit == 1):
		turnRight()
	else:
		turnLeft()
	forwardMotor1(400)
	if ((standard.digital_read(pinIrIzq) == LINEA) or (standard.digital_read(pinIrDer) == LINEA)):
		searching = False
