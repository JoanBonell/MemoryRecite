# Project Objectives

## Project purpose statement
The purpose of this project is to develop an AI-powered application that helps users memorize legal text by providing an interactive platform for recitation and feedback.
The application allows users to upload a PDF containing the legal material they need to memorize. It then processes the document and enables the user to recite the content from memory. Using voice recognition and natural language processing, the application listens to the user's recitation, transcribes it, and compares it with the original text. Upon completion, it provides detailed feedback on the user's performance, including the percentatge of accuracy and specific areas where errors or omissions occurred.

## In scope (Features to include):
### 1. PDF Upload and Text Extraction:
- Functionality for users to upload PDF documents containing legal texts.
- Extraction of text from PDFs using libraries such as PyPDF2 or pdfminer.six
- Handling of text encoding and accented characters relevant to the language of the legal text.

### 2. Text Preprocessing and cleaning:
- Removal of unwanted elements like headers, footers, page numbers, and excessive whitespace.
- Normalization of text for consistent formatting.
- Tokenization of text into sentences and words using NPL (Natural Processing Language) libraries.

### 3. Voice Recognition and Transcription:
- Capture of audio input from the user during recitation.
- Transcription of spoken words into text using voice recognition libraries like SpeechRecognition and PyAudio.
- Handling of real-time or near-real-time transcription needs.

### 4. Natural Language Processing (NLP):
- Processing of both the original text and the user's transcribed recitation.
- Implementation of tokenization, lemmatization, and stop-word removal to prepare text for comparison.
- Use of NLP techniques to improve the accuracy of text comparison.

### 5. Comparison and Evaluation Algorithm:
- Development of an algoritm to compare the user's recitation with the original text.
- Calculation of similarity metrics, such as Cosine Similarity, to determine the percentage of accuracy.
- Identification of specific errors or omissions in the user's recitation.

### 6. User Interface Design:
- Creation of a user-friendly interface for desktop use.
- Implementation of features like PDF Upload Buttons, start/stop recitation controls, and result displays.
- Use of GUI frameworks like Tkinter or PyQt for interface development.

### 7. Feedback and Reporting:
- Presentation of detailed feedback, including overall accuracy percentages.
- Highlighting of specific sections where mistakes or omissions occurred.
- Options to save or export results for future reference.

### 8. Error Handling and Logging:
- Implementation of robust error handling to manage exceptions gracefully.
- Logging of significant events and errors to assist in debbuging and user support.

### 9. Testing and Validation:
- Development of unit and integration test to ensure each module functions correctly.
- Testing with a variety of PDFs to ensure robustness and reliability.

## Out of Scope (Features to exclude Initially)

### 1. Advanced Machine Learning Models:
- Development of custom machine learning models for voice recognition or NPL beyond existing libraries.
- Implementation of semantic analysis or understanding of paraphrased content.

### 2. Support for Multiple Languages:
- Handling of languages other than the initial target language (Spanish at launch).

### 3. Mobile Platform Support: 
- Development of mobile appliactions for iOS or Android devices.
- Optimization of the interface and functionality for mobile use.

### 4. Optical Character Recognition (OCR):
- Processing of scanned PDFs or image-based documents using OCR technologies.
- Integration with tools like Tesseract OCR for handling non-text PDFs

### 5. Database Integration and User Management:
- Implementation of databases for storing user profiles, session histories, or progress tracking.
- Features related to user authentication, account creation, or personalized settings.

### 6. Real-time feedback and Correction:
- Providing immediate corrections or suggestions during the user's recitation.
- Interrupting the user to point out errors in real-time.

### 7. Advanced Security Measures:
- Incorporation of encryption protocols beyond standard practices for local applications.
- Compliance with specific data protection regulations (e.g, GPDR) unless necessary.

### 8. Third-party Service Integrations:
- Integration with external APIs or services beyond essential libraries (e.g, cloud storage, social media sharing).
- Use of paid services requiring ongoing subscriptions or fees.

### 9. Extensive User Customization:
- Features allowing extensive customization of the application's interface or functionality.
- Modular plugins or extensions for added features.

### 10. Scalability for High User Loads:
- Preparation for deploymebnt scenarios requiring of large numbers of concurrent users.
- Optimization for server-based deployment or cloud scalability.

# Gather Functional Requirements

## List of all the functionalities that the application must have categorized:

### 1. PDF Upload Functionality

Users can upload PDF documents containing legal texts.

### 2. Text Extraction from PDFs

The application extracts text accurately from uploaded PDFs.

### 3. Text Cleaning and Preprocessing

Removal of unwanted elements (headers, footers, page numbers).

### 4. Voice recognition and transcription

Capture user recitation via microphone.
Transcribe spoken words into text accurately.

### 5. Natural Language Processing (NLP)

Tokenization, lemmatization, and stop-word removal. Preparation of text for comparison.

### 6. Text comparison Algorithm
Compare transcribed text with the original text and calculate similarity percentage.

### 7. Feedback generation:

Provide detailed feedback highlighting errors or omisions and display overall accuracy percentage.

### 8. User Interface (UI)

Simple and intuitive interface for desktop use and controls for starting and stopping recitation.

### 9. Error Handling

Graceful handling of exceptions and errors and user-friendly error messages.

## Should-have (Important but not critical)

### 1. Selective text sections
Ability to select specific sections of the text to focus on that part by the user.

### 2. Process Tracking
Track user performance over time and display historical accuracy data.

### 3. Support for Multiple Languages
Initial support for one language with planned expansion. The initial language is of voice recognition is going to be Spanish.

### 4. Customization Options
Adjust the sensitivity of text comparison and personalize feedback settings.

### 5. Offline Functionality
Allow usage without an internet connection after setup

### 6. Export Results
Option to save or export feedback reports

## Nice-to-have (Enhacements)
### 1. Mobile compatibility
Develop a mobile-friendly version or app.
### 2. Real-time feedback
Provide immediate feedback during recitation.
### 3. Integration with learning platforms
Connect with educational tools or LMS systems (dudasoposicion.es)
### 4. Gamification elements 
Include achievements or rewards for milestones.
### 5. Social Sharing
Share progress or results on social media.
### 6. Multi-user Support
Profiles for different users on the same device.

# Gather Non-Functional Requirements

## Performance Requirements
### 1. Processing Speed
The application should process and provide feedback withing 5 seconds after recitation ends.
### 2. Resource Utilization
Efficient use of system resources to prevent slowdowns.
### 3. Scalability
Able to handle larger texts without a significant performance degradation.

## Usability Requirements
### 1. User-friendly Interface
Intiutive navigation with minimal learning curve.
### 2. Accessibility
Support for users with disabilities (e.g., compatible with screen readers).
### 3. Scalability
Able to handle larger texts without significant performance degradation.
## Security Requirements
### 1. Data Privacy
User data (e.g., Recitations, results) must be stored securely.
### 2. Compliance
Comply with relevant data protection regulations (e.g., GPDR if applicable).
### 3. Local Data Storage
Prefer storing data locally on the user's device to enhance privacy.

## Reliability Requirements
### 1. Error Recovery
Application should handle unexpected inputs or failures gracefully.
### 2. Availability
High availability with minimal crashes or downtime.
### 3. Data Integrity
Ensure that data is not corrupted during processing.

## Mantainability Requirements
### 1. Modular Design
Code should be organized for easy updates and maintenance.
### 2. Documentation
Comprehensive documentation for future development and troubleshooting.

## Portability Requirements
### 1. Platform Compatibility
Support for major desktop operating systems (Windows, macOS, Linux).
### 2. Installation Ease
Simple installation process without complex dependencies.

## Performance Metrics
### 1. Accuracy of Voice Recognition
Aim for at least 90% accuracy in transcriptions under optimal conditions.
### 2. Text Comparison Sensitivity
Ability to detect omissions, insertions, and substitutions accurately.

## User Experience Requirements
### 1. Feedback Clarity
Feedback should be presented in an understandable and actionable manner.
### 2. Response Time
UI elements should respond within 1 second to user interactions.


## Legal and Ethical Requirements
### 1. Content Ownership
Respect copyrights of uploaded PDFs; user is responsible for having rights to the content.

### 2. Ethical Use
Ensure the application is used for legitimate educational or professional purposes.
