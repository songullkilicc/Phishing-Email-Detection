import re
import base64

def find_links(text):
    """Extracts links from email text"""
    links = re.findall(r'https?://\S+', text)
    return links

suspicious_keywords = [
    "verify your account",
    "urgent",
    "click here",
    "login immediately",
    "account suspended",
    "reset password",
    "security alert"
]

def score_email(text):
    """Scores the email based on suspicious keywords"""
    score = 0
    text_lower = text.lower()
    
    for keyword in suspicious_keywords:
        if keyword in text_lower:
            score += 10
    
    links = find_links(text_lower)
    score += len(links) * 20
    
    return score

def encrypt_text(text):
    """Encodes text to Base64"""
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def main():
    with open("sample_email.txt", "r", encoding="utf-8") as f:
        email_content = f.read()
    
    print("E-mail içeriği:\n")
    print(email_content)

    links = find_links(email_content)
    print("\n🔗 Bulunan Linkler:")
    for link in links:
        print(link)
    
    total_score = score_email(email_content)
    print(f"\n📊 Toplam Phishing Skoru: {total_score}")

    threshold = 50
    if total_score >= threshold:
        print("\n⚠️ Uyarı: Bu e-mail phishing olabilir!")
    else:
        print("\n✅ Bu e-mail muhtemelen güvenli.")
    
    # Şifreleme demo:
    encrypted_content = encrypt_text(email_content)
    print("\n🔐 Şifrelenmiş E-mail İçeriği (Base64):")
    print(encrypted_content)

if __name__ == "__main__":
    main()


"""
"This Python script reads the content of an email from a text file, 
extracts any URLs, and checks for suspicious keywords typically found in phishing emails. 
It then calculates a phishing risk score based on these criteria.
 If the score exceeds a certain threshold, the script warns that the email might be a phishing attempt.


Additionally, as a simple demonstration of data privacy, 
the email content is encoded in Base64 format to show how sensitive information can be encrypted."
"""


