from cryptography.hazmat.primitives import hashes

def get_shas(cleartext):
	
	res={
		'SHA-1':hashes.Hash(hashes.SHA1()),
		'SHA-224':hashes.Hash(hashes.SHA224()),
		'SHA-256':hashes.Hash(hashes.SHA256()),
		'SHA512-224':hashes.Hash(hashes.SHA512_224()),
		'SHA3-256':hashes.Hash(hashes.SHA3_256()),
		'SHA3-512':hashes.Hash(hashes.SHA3_512())
	}
	bs=bytes(cleartext.encode(encoding="utf-8"))
	for __key in res:
		res[__key].update(bs)
		res[__key]=res[__key].finalize().hex()
	
	return res
