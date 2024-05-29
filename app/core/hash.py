import hashlib



def generate_password_hash(password:str) -> str:
	return hashlib.sha256(password.encode('ASCII')).hexdigest()

def check_password_hash(password:str, password_hash:str) -> bool:
	return hashlib.sha256(password.encode('ASCII')).hexdigest() == password_hash 