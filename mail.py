import pandas as pd
import os
import numpy as np
# import tensorflow_hub as hub
# import tensorflow_text as text
# import faiss
import email
# from email import policy
# from sklearn.metrics.pairwise import cosine_similarity

def get_email(email_path):
    with open(email_path, "r", encoding = "ISO-8859-1") as mail:
        email_content = mail.read()
        return email_content
    
    
def get_emails_paths(path):
    email_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.startswith('.'):
                email_path = os.path.join(root, file)
                email_paths.append(email_path)
    return email_paths
    
path = "data/archives-EGC/"
emails = get_emails_paths(path)


# Vérifier les differents types de contenu (Content-Type)
content_types = []
for msg in emails:
  msg = email.message_from_string(msg)
  content_type = msg.get_content_type()
  if content_type not in content_types:
    content_types.append(content_type)
# print(content_types)


content_types = []
for msg in emails:
  msg = email.message_from_string(msg)
  content_type = msg.get_content_type()
  if content_type == 'multipart/related':
    for part in msg.walk():
         if part.get_content_type() == "text/plain":
          # Récupération du corps du message
            body = part.get_payload(decode=True).decode(part.get_content_charset())
        #   return body
        # body = msg.get_payload(0).get_payload(decode=True)
            print(body)
            break



