import re

def convert_bangla_text(text):
    # বাংলা ইউনিকোড ফন্ট বিকৃত করার জন্য সম্ভাব্য লজিক
    # আকার-ইকার উল্টানো (এই লজিক ভবিষ্যতে আরও উন্নত করা যেতে পারে)
    replace_map = {
        "া": "◌া", "ি": "◌ি", "ী": "◌ী", "ু": "◌ু", "ূ": "◌ূ", "ে": "◌ে", "ৈ": "◌ৈ", "ো": "◌ো", "ৌ": "◌ৌ"
    }
    
    # চিহ্ন সংরক্ষণ করা যাতে ফন্ট বিকৃতি না হয়
    text = re.sub(r'([,।!?])', r' \1 ', text)  # চিহ্নের আগে-পরে স্পেস যোগ করা
    
    converted_text = "".join(replace_map.get(char, char) for char in text)
    return converted_text.strip()

# ইউজার ইনপুট নেওয়া ও কনভার্ট করা
if __name__ == "__main__":
    print("বাংলা লেখা দিন (শেষ করতে 'exit' লিখুন):")
    while True:
        try:
            user_input = input("👉 আপনার লেখা: ")
            if user_input.lower() == "exit":
                print("🚀 প্রোগ্রাম বন্ধ করা হচ্ছে...")
                break
            print(f"✅ কনভার্ট করা লেখা: {convert_bangla_text(user_input)}\n")
        except EOFError:
            print("⚠️ ইনপুট নেওয়া সম্ভব নয়! প্রোগ্রাম বন্ধ হচ্ছে...")
            break
