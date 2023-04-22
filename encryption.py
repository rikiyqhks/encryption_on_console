import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# 入力を受け取る
input_str = input("文字列を入力してください：")

# 暗号化方式を選択する
while True:
    encryption_method = input("暗号化の方法を選択してください（AES or ハッシュ）：")
    if encryption_method.lower() == "aes":
        key = get_random_bytes(16)  # AESの鍵長は16バイト
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(input_str.encode('utf-8'))
        print("AESで暗号化した結果：")
        print("鍵：", key)
        print("暗号文：", ciphertext)
        print("タグ：", tag)
        break
    elif encryption_method.lower() == "ハッシュ":
        salt = hashlib.sha256(get_random_bytes(32)).hexdigest().encode('utf-8')
        hashed = hashlib.pbkdf2_hmac('sha256', input_str.encode('utf-8'), salt, 100000)
        print("ハッシュ化した結果：")
        print("ソルト値：", salt)
        print("ハッシュ値：", hashed)
        break
    else:
        print("正しい暗号化方式を入力してください。")
