# Project Objectives

## Project purpose statement
The purpose of this project is to develop an AI-powered application that helps users memorize legal text by providing an interactive platform for recitation and feedback.
The application allows users to upload a PDF containing the legal material they need to memorize. It then processes the document and enables the user to recite the content from memory. Using voice recognition and natural language processing, the application listens to the user's recitation, transcribes it, and compares it with the original text. Upon completion, it provides detailed feedback on the user's performance, including the percentatge of accuracy and specific areas where errors or omissions occurred.

## In scope (Features to include):
1. PDF Upload and Text Extraction:
- Functionality for users to upload PDF documents containing legal texts.
- Extraction of text from PDFs using libraries such as PyPDF2 or pdfminer.six
- Handling of text encoding and accented characters relevant to the language of the legal text.

2. Text Preprocessing and cleaning:
- Removal of unwanted elements like headers, footers, page numbers, and excessive whitespace.
- Normalization of text for consistent formatting.
- Tokenization of text into sentences and words using NPL (Natural Processing Language) libraries.

3. Voice Recognition and Transcription:
- Capture of audio input from the user during recitation.
- Transcription of spoken words into text using voice recognition libraries like SpeechRecognition and PyAudio.
- Handling of real-time or near-real-time transcription needs.

4. Natural Language Processing (NLP):
- Processing of both the original text and the user's transcribed recitation.
- Implementation of tokenization, lemmatization, and stop-word removal to prepare text for comparison.
- Use of NLP techniques to improve the accuracy of text comparison.

5. Comparison and Evaluation Algorithm:
- Development of an algoritm to compare the user's recitation with the original text.
- Calculation of similarity metrics, such as Cosine Similarity, to determine the percentage of accuracy.
- Identification of specific errors or omissions in the user's recitation.

6. User Interface Design:
- Creation of a user-friendly interface for desktop use.
- Implementation of features like PDF Upload Buttons, start/stop recitation controls, and result displays.
- Use of GUI frameworks like Tkinter or PyQt for interface development.

7. Feedback and Reporting:
- Presentation of detailed feedback, including overall accuracy percentages.
- Highlighting of specific sections where mistakes or omissions occurred.
- Options to save or export results for future reference.

8. Error Handling and Logging:
- Implementation of robust error handling to manage exceptions gracefully.
- Logging of significant events and errors to assist in debbuging and user support.

9. Testing and Validation:
- Development of unit and integration test to ensure each module functions correctly.
- Testing with a variety of PDFs to ensure robustness and reliability.

## Out of Scope (Features to exclude Initially)

1. Advanced Machine Learning Models:
- Development of custom machine learning models for voice recognition or NPL beyond existing libraries.
- Implementation of semantic analysis or understanding of paraphrased content.

2. Support for Multiple Languages:
- Handling of languages other than the initial target language (Spanish at launch).

3. Mobile Platform Support: 
- Development of mobile appliactions for iOS or Android devices.
- Optimization of the interface and functionality for mobile use.

4. Optical Character Recognition (OCR):
- Processing of scanned PDFs or image-based documents using OCR technologies.
- Integration with tools like Tesseract OCR for handling non-text PDFs

5. Database Integration and User Management:
- Implementation of databases for storing user profiles, session histories, or progress tracking.
- Features related to user authentication, account creation, or personalized settings.

6. Real-time feedback and Correction:
- Providing immediate corrections or suggestions during the user's recitation.
- Interrupting the user to point out errors in real-time.

7. Advanced Security Measures:
- Incorporation of encryption protocols beyond standard practices for local applications.
- Compliance with specific data protection regulations (e.g, GPDR) unless necessary.

8. Third-party Service Integrations:
- Integration with external APIs or services beyond essential libraries (e.g, cloud storage, social media sharing).
- Use of paid services requiring ongoing subscriptions or fees.

9. Extensive User Customization:
- Features allowing extensive customization of the application's interface or functionality.
- Modular plugins or extensions for added features.

10. Scalability for High User Loads:
- Preparation for deploymebnt scenarios requiring of large numbers of concurrent users.
- Optimization for server-based deployment or cloud scalability.