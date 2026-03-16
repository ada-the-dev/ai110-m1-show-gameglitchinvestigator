# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    Overall, the user interface was visually simple and intuitive. Upon running the application, values were not updated nor displayed correctly, the game's difficulty settings did not incrementally become more difficult, and hints based on the user's input (guesses) were given inconsistently. Not all input given by the user was displayed in the history data structure within the "developer debug info" window. The "New Game" button did not restart the game in a fresh state either.
- List at least two concrete bugs you noticed at the start (for example: "the hints were backwards").
    When increasing the game's difficulty from normal to hard, the numerical range for guessing values did not increase. When increasing the game's difficulty from easy to normal, the given attempts increased. I expect that the numerical ranges increase, and that the given attempts decrease when game difficulty increases.

    Adding on, the secret number for a game is not guarenteed to be within the range of that game's difficulty.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I used Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    It was correct in detecting that values were hard-coded when generating a secret number. It suggested that we used pre-existing values associated with the selected difficulty. I verified this by looking at the code.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    The AI suggested an incorrect function definition written under the premise that string comparison could occur even though it was verified through earlier fixes that this would not happen. I looked at the code and talked with the AI to verify this.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I tested the game and verified code logic manually in the terminal or coding window.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
    I tested wheter or not the displayed range values changed with a selected difficulty level manually after fixing this error. This showed that the code was not calculating the correct values to be displayed.
- Did AI help you design or understand any tests? How?
    Yes, it did. It generated the tests, and I verified via questioning it to see how the tests worked, and what it tested against.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    When Streamlit reruns, it regenerates the entire page. A session state helps preserve values between these regenerations.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      I want to continue questioning the AI.
- What is one thing you would do differently next time you work with AI on a coding task?
    One thing I would do differently is use the AI to familiarize myself with the codebase more.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    I learned that AI generated code streamlines project building a lot more than I thought.
