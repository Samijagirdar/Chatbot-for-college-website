College Enquiry Chatbot 🤖
This is a chatbot application designed specifically for college enquiries. It provides information about various aspects of the college, such as courses, admissions, faculty, facilities, and more. This documentation provides an overview of the project structure, installation instructions, usage guidelines, testing information, contribution guidelines, and licensing details.

## Project Structure 📁

```bash
+---backend
|   +---app
|   |       app.py
|   |       greetings.py
|   |       spelling_fix.py
|   |
|   +---data
|   |       data.py
|   |       generate_data.py
|   |       intends.json
|   |       querys.json
|   |       raw_data.json
|   |       related.json
|   |       responses.json
|   |
|   +---models
|   |   |   interpreter.py
|   |   |
|   |   +---saved
|   |   |       default_lemmatize.json
|   |   |       default_stem.json
|   |   |       new_lemmatize.json
|   |   |       new_stem.json
|   |   |       test.json
|   |   |
|   |   +---sequence_to_vector
|   |   |       seq2vec.py
|   |   |       utils.py
|   |   |
|   |   +---vector_to_class
|   |           utils.py
|   |           vec2class.py
|   |
|   +---tests
|           interpreter_test.py
|
+---frontend
    +---public
    |       background.png
    |       favicon.ico
    |       index.html
    |       logo192.png
    |       logo512.png
    |       manifest.json
    |       robots.txt
    |
    +---src
        |   App.css
        |   App.jsx
        |   App.test.js
        |   index.css
        |   index.js
        |   logo.svg
        |   reportWebVitals.js
        |   setupTests.js
        |
        +---api
        |       chatApi.js
        |
        +---components
            +---chat
            |       chat.css
            |       chat.jsx
            |
            +---chatbox
            |       chatbox.css
            |       chatbox.jsx
            |
            +---info
                    info.css
                    info.jsx

