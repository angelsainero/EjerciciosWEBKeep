usuarios = (
    ("pigmonchu", "lolailo1970"),
    ("genaro23", "1234abc$"),
    ("arrumako", "killo.2018"),
)

strUser = input("User....: ")
strPwd =  input("Password: ")

ix = 0
while ix < len(usuarios) and usuarios[ix][0] != strUser:
  ix += 1
    
if ix == len(usuarios):
  print("No te conozco, no pasas")
else:
  if usuarios[ix][1] == strPwd:
    print("Entró en el sistema")
  else: 
    print("No te conozco, no pasas") # Mismo mensaje que usuario desconocido para no dar pistas a los hackers