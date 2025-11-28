
import json
# image of the cypher
try:
    with open('words_dictionary.json', 'r') as f:
        words = json.load(f)
except FileNotFoundError:
    # Fallback: use a basic English word set
    words = {}
    print("Warning: words_dictionary.json not found. Using basic validation.")

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alpha_dict = {
    'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,
    'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1
}


def encrypt(text, key):
    return shift(text, key)


def decrypt(text, key):
    return shift(text, len(alpha) - key)


def shift(text, shift_amount):
    result = ''
    
    for char in text:
        lower_char = char.lower()
        
        # Keep non-alphabet characters as is
        if lower_char not in alpha_dict:
            result += char
            continue
        
        # Shift the character
        old_index = ord(lower_char) - ord('a')
        new_index = (old_index + shift_amount) % len(alpha)
        result += alpha[new_index]
    
    return result


def brute_force_decrypt(text):
    possible_messages = []
    
    for key in range(1, len(alpha)):
        decrypted_msg = decrypt(text, key)
        words_in_msg = decrypted_msg.split()
        
        # Check validity using dictionary lookup
        valid_word_count = 0
        for word in words_in_msg:
            clean_word = word.strip('.,!?;:').lower()
            if clean_word in words:
                valid_word_count += 1
        
        match_percentage = (valid_word_count / len(words_in_msg) * 100) if words_in_msg else 0
        
        possible_messages.append({
            'key': key,
            'message': decrypted_msg,
            'validWordCount': valid_word_count,
            'matchPercentage': match_percentage
        })
    
    # Sort by match percentage (descending)
    possible_messages.sort(key=lambda x: x['matchPercentage'], reverse=True)
    
    return possible_messages


def example():
    
    msg = 'Hello world !'
    
    longer_msg = ('The European languages are members of the same family. '
                  'Their separate existence is a myth. For science, music, sport, etc, '
                  'Europe uses the same vocabulary. The languages only differ in their '
                  'grammar, their pronunciation and their most common words. Everyone '
                  'realizes why a new common language would be desirable: one could refuse '
                  'to pay expensive translators. To achieve this, it would be necessary to '
                  'have uniform grammar, pronunciation and more common words. If several '
                  'languages coalesce, the grammar of the resulting language is more simple '
                  'and regular than that of the individual languages. The new common language '
                  'will be more simple and regular than the existing European languages. '
                  'It will be as simple as Occidental; in fact, it will be Occidental. '
                  'To an English person, it will seem like simplified English, as a skeptical '
                  'Cambridge friend of mine told me what Occidental is.The European languages '
                  'are members of the same family. Their separate existence is a myth. '
                  'For science, music, sport, etc, Europe uses the same vocabulary. '
                  'The languages only differ in their grammar, their pronunciation and their '
                  'most common words. Everyone realizes why a new common language would be '
                  'desirable: one could refuse to pay expensive translators.')
    
    key = 23
    
    print("Original Message:", msg)
    
    # Encrypt
    encrypted_msg = encrypt(msg, key)
    longer_encrypted_msg = encrypt(longer_msg, key)
    
    print('Encrypted Message:', encrypted_msg)
    
    # Decrypt with known key
    decrypted_msg = decrypt(encrypted_msg, key)
    
    print('Decrypted Message:', decrypted_msg)
    
    # Brute force attack
    brute_force_results = brute_force_decrypt(encrypted_msg)
    longer_brute_force_results = brute_force_decrypt(longer_encrypted_msg)
    
    print('\nBrute Force Decryption Results:')
    for result in brute_force_results[:5]:  # Show top 5
        print(f"  Key {result['key']}: {result['message'][:50]}... "
              f"({result['matchPercentage']:.1f}% match)")
    
    print('\nLonger Brute Force Decryption Results (Top 3):')
    for result in longer_brute_force_results[:3]:
        print(f"  Key {result['key']}: {result['message'][:50]}... "
              f"({result['matchPercentage']:.1f}% match)")


example()