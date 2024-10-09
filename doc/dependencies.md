# Dependencies

- Text Extraction depends on PDF upload being implemented.
- Text Cleaning and Preprocessing depends on successfull text extraction, we need to be sure that text extraction algorithm has no errors in any case.
- NLP Processing requires Text Cleaning and Preprocessing to be completed.
- Voice Recognition and Transcription depends on access to microphone hardware.
- Text Comparison Algorithm requires both NLP Processing and Voice Recognition and Transcription outputs.
- Feedback Generation depends on the results from the Text Comparison Algorithm.



# Analysis of functionalities and Features

## Feature Breakdown
We'll break down each functionality into smaller tasks to make them more manageable.

### 1. PDF Upload Funcionality
- Design the UI Component for file selection (e.g., "Upload PDF" button)
- Implement a file browser dialog to select PDF files
- Validate the selected file (check for correct format and accessibility)
- Provide feedback to the user upon successfull upload or error

### 2. Text Extraction from PDFs
- Integrate a PDF parsing library (e.g., PyPDF2, pdfminer.six).
- Develop functions to read and extract text from the PDF.
- Handle various PDF formats (text-based, scanned images).
- Implement error handling for corrupted or encrypted PDFs.

### 3. Text Cleaning and Preprocessing
- Remove unwanted elements (headers, footers, page numbers).
- Normalize text (remove extra spaces, line breaks).
- Handle character encoding and special characters.
- Convert text to a consistent case (e.g., all lowercase).

### 4. Voice Recognition and Transcription
- Set up microphone access and permissions.
- Integrate a speech recognition library (e.g., SpeechRecognition, PyAudio).
- Implement functionality to capture audio input.
- Transcribe audio to text in real-time or post-recording.
- Handle exceptions and errors in voice recognition.

### 5. Natural Language Processing (NLP)
- Integrate NLP libraries (e.g., NLTK, spaCy).
- Tokenize text into sentences and words.
- Remove stop words from the text.
- Apply lemmatization or stemming.
- Prepare the text data for comparison.

### 6. Text Comparison Algorithm
- Choose an appropiate similarity metric (e.g., Cosine Similarity).
- Implement the comparison algorithm.
- Calculate similarity scores between original and recited text.
- Identify specific errors, omissions, or additions.

### 7. Feedback generation
- Design a format for presenting feedback.
- Summarize overall performance (e.g., percentage of accuracy).
- Highlight specific areas where the user deviated from the text.
- Provide suggestions for improvement.

### 8. User Interface (UI)
- Design the layout and navigation flow.
- Implement UI components (buttons, progress bars, text displays).
- Ensure the UI is responsive and user-friendly.
- Integrate UI with backend functionalities.


### 9. Error Handling and Logging
- Implement exception handling throughout the application.
- Provide clear and helpful error messages to the user.
- Log errors for debbuging and maintenance.
- Implement a logging system (e.g., using Python's logging module).

### 10. Selective Text Sections (Should-have)
- Allow users to select specific sections of the text.
- Update processing functions to handle selected text.
- Modify UI to support text selection.

### 11. Progress Tracking (Should-have)
- Store user performance data over time.
- Implement data visualization for progress (charts, graphs).
- Provide options to view past results.

### 12. Customization Options (Should-have)
- Allow users to adjust settings (e.g., sensitivity of comparison).
- Implement a settings menu in the UI.
- Store user preferences.

### 13. Export Results (Should-have)
- Provide functionality to save feedback reports.
- Support different export formats (PDF, CSV).
- Implement UI options for exporting data.

# Prioritize Features (MoSCoW Method)

Using MoSCoW method, we'll categorize features as Must-Have (M), Should-Have (S), Could-Have (C), and Wont-Have (W) for the initial release.

## Must-Have

- PDF Upload Functionality
- Text Extraction from PDFs
- Text Cleaning and Preprocessing
- Voice Recognition and Transcription
- Natural Language Processing (NLP)
- Text Comparison Algorithm
- Feedback Generation
- User Interface (UI)
- Error Handling and Logging

## Should-Have
- Selective Text Sections
- Progress Tracking
- Customization Options
- Export Results

## Could-Have

- Real-time Feedback
- Offline functionality
- Support for Multiple Languages

## Wont-have (for initial release)
- Mobile Compatibility
- Integration with Learning Platforms
- Gamification Elements
- Social Sharing Features




