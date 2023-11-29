from pyVoIP.VoIP import VoIPPhone, InvalidStateError

def answer(call): # This will be your callback function for when you receive a phone call.
    try:
      call.answer()
      call.hangup()
    except InvalidStateError:
      pass
  
if __name__ == "__main__":
    phone=VoIPPhone("192.168.178.1", 5060, "simonkuhlo", "sehr geheim", callCallback=answer, myIP="192.168.178.59", sipPort=5060)
    phone.start()
    input('Press enter to disable the phone')
    phone.stop()