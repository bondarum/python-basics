import ex12_module_words

sentence = "All good things come to those who wait."
words = ex12_module_words.break_words(sentence)
print words

sorted_words = ex12_module_words.sort_words(words)
print sorted_words

ex12_module_words.print_first_word(words)
ex12_module_words.print_last_word(words)
print words

ex12_module_words.print_first_word(sorted_words)
ex12_module_words.print_last_word(sorted_words)
print sorted_words

sorted_words = ex12_module_words.sort_sentence(sentence)
print sorted_words

ex12_module_words.print_first_and_last(sentence)
ex12_module_words.print_first_and_last_sorted(sentence)

# Workshop time! ws1_fix_code.py
