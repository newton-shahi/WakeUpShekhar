# Shekhar: Bilingual Wake Word Listener

A lightweight, completely client-side bilingual wake word detection application that listens for triggers in English (**"Hey Shekhar"**) and Nepali (**"Namaste Shekhar"**). 

This project is entirely **rules-based**, relying on fundamental string distance algorithms and fuzzy token matching instead of heavy machine learning frameworks or cloud-based neural networks. This makes it highly efficient, secure, and ready to run inside any standard modern web browser.

---

## 📝 What It Does
This application listens to continuous microphone input, converts your spoken words into text in real-time, and triggers an action (like waking up an assistant) when it hears the target phrase. 

---

### How it does it
The pipeline follows a step-by-step evolutionary learning roadmap built across individual Python prototypes included in this repository so that learning is easier:

1. **Normalization (`G11`)**: Cleans raw input text by forcing it to lowercase, stripping punctuation/symbols using regex, and collapsing duplicate spaces into a single space.
2. **Exact Matching (`G12`, `G13`)**: Scans the cleaned text tokens to find direct substring occurrences of target phrases, organized within a clean object-oriented class wrapper tracking metrics.
3. **Levenshtein Distance (`G14`)**: Implements a standard dynamic programming matrix algorithm to compute the exact edit distance (minimum insertions, deletions, and substitutions) between two arbitrary strings.
4. **Fuzzy Checking (`G15`)**: Splits text into structural tokens and evaluates whether any sequence matches target words within an acceptable variation threshold (e.g., accepting typo variations like `"guuud"` for `"good"` or `"byad"` for `"bad"`).
5. **Scoring Logic (`G16`)**: Introduces weighted penalty metrics where closer matches yield scores nearing `1.0`, enabling confident threshold triggers.

The final client implementation (`index.html`) translates these modular concepts into pure vanilla JavaScript inside a continuous speech recognition event loop.

---

##  Why It Does It
* **Zero ML Overhead:** Runs entirely in the browser without needing massive neural network libraries or backend servers.
* **Speed & Efficiency:** Near-instantaneous matching with minimal CPU and memory usage.
* **Privacy-Focused:** Processes audio locally within the browser.

##  How to Open the Files

### Running the Final Project
To run the main application:
1. Locate the `index.html` file in the root directory.
2. Double-click `index.html` to open it directly in any modern web browser (Google Chrome, Microsoft Edge, etc.).
3. Grant microphone permissions when prompted by your browser and start speaking.

### Learning the Concepts Step-by-Step
The project includes an incremental curriculum designed to build up the final implementation step-by-step:

* **`G11learnnormalize.py`**: Clean text string data formatting using Python regular expressions (`re`).
* **`G12learnExact.py`**: Baseline sub-phrase evaluation against defined keyword dictionaries.
* **`G13classWakeup.py`**: Refactoring exact match routines into reusable Python classes that track lifetime execution states and detection counters.
* **`G14levenshtein.py`**: Implementation of the matrix-based string edit-distance algorithm.
* **`G15fuzzyChecker.py`**: Combining string tokenization with distance thresholds to find approximate array matches.
* **`G16Scoring.py`**: Integrating inverse-distance mathematical confidence ratios to calculate concrete numeric scores.
* **`index.html`**: The unified client application bundling a glowing reactive CSS UI, continuous Web Speech bindings, and the ported JavaScript fuzzy-matching logic.
---

### 🙏 Reference
Learned from and inspired by [santabasnet/WakeUpDeepa](https://github.com/santabasnet/WakeUpDeepa).