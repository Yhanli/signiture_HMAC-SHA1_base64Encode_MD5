

import hashlib
import base64
import hmac


def Get_base64encode(encode_item):
    encoded = base64.b64encode((encode_item.encode('utf-8')))
    return str(encoded,'utf-8')


def Get_Hmac_sha1(Hmac_item,sha1Key):
    digester = hmac.new(bytes(sha1Key,'utf-8'),bytes(Hmac_item,'utf-8'),hashlib.sha1)
    return digester.digest()


def Get_signatur_inMD5(digester):
    signature = hashlib.md5(digester)
    return signature.hexdigest()

if __name__ == '__main__':
    # test sample should get 2a61f17a02b9161080bb417fb1147c60, this test sample used public information provided by ximalaya.com developer document

    app_id = 'b617866c20482d133d5de66fceb37da3'
    app_sec = '4d8e605fa7ed546c4bcb33dee1381179'
    timeStamp ='1533203363618'
    nonce = 'd15d792875807b0fec620f4db2ac1667'
    serverAuthenticateStaticKey = 'z0hh5l9A'
    sig_attributes = 'app_key=b617866c20482d133d5de66fceb37da3&calc_dimension=1&category_id=0&client_os_type=4&count=20&nonce=d15d792875807b0fec620f4db2ac1667&page=1&q=聪明与智慧&timestamp=1533203363618'
    sha1Key = app_sec + serverAuthenticateStaticKey

    _base64encoding = Get_base64encode(sig_attributes)
    _hmac = Get_Hmac_sha1(_base64encoding, sha1Key)

    _signature = Get_signatur_inMD5(_hmac)

    print(_signature)



