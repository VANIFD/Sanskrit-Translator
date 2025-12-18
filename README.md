# Sanskrit-Translator
Sanskrit Multi-language Translator

🌐 Description:
This project is a web-based Sanskrit translator built with Streamlit. Users can input a Sanskrit word and select a target language to get translations in 20+ languages. The app features a modern, sleek UI, professional layout, and a ready-to-use dataset of 50 Sanskrit words.

Features

Translate Sanskrit words to English, Hindi, Tamil, Kannada, Telugu, Malayalam, Marathi, Gujarati, Punjabi, Bengali, Odia, Urdu, French, German, Spanish, Italian, Portuguese, Russian, Japanese, and Chinese.

Sleek dark-gradient UI with rounded input boxes and buttons.

Dropdown to select the target language.

Dynamic success/error messages for better user experience.

Ready-to-use JSON dataset for fast translations.

Professional layout suitable for presentations or demos.

Folder Structure
Sanskrit-Translator/
│
├── app.py                  # Main Streamlit app
├── data/
│   └── translations.json   # Sanskrit word translations
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


Installation

1. Clone the repository:
git clone https://github.com/vani/Sanskrit-Translator.git
cd Sanskrit-Translator

2. Create a virtual environment and activate it:
python -m venv myenv
# Windows
myenv\Scripts\activate

3. Install required packages:
pip install -r requirements.txt

4.Run the Streamlit app:
streamlit run app.py

5. In the web interface:

Enter a Sanskrit word in the input box.

Select the target language from the dropdown.

Click Translate to see the translated word.

6. Customization

Add more Sanskrit words or languages by editing data/translations.json.

Change the background, colors, or layout by modifying CSS in app.py.

Add advanced features like copy-to-clipboard, recent searches, or auto-suggestions.

7.Dependencies

Python 3.8+

Streamlit

JSON (built-in)
