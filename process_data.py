import pandas as pd

english_file = 'europarl-v7.EN-FR/europarl-v7.fr-en.en.aligned.tok'
french_file = 'europarl-v7.EN-FR/europarl-v7.fr-en.fr.aligned.tok'
dat_file = 'europarl-v7.EN-FR/europarl-v7.fr-en.dat'

#load files 
with open(french_file, 'r', encoding='utf-8') as f:
    french_sentences = [line.strip() for line in f]

with open(english_file, 'r', encoding='utf-8') as f:
    english_sentences = [line.strip() for line in f]

with open(dat_file, 'r', encoding='utf-8') as f:
    dat_lines = [line.strip() for line in f]

#if this is false i'm gonna call rabinovich and just start crying 
assert len(french_sentences) == len(english_sentences) == len(dat_lines), ":("

data = []
for french, english, dat_line in zip(french_sentences, english_sentences, dat_lines):
    native_language = dat_line.split('LANGUAGE="')[1].split('"')[0]
    
    #determine if a sentence has been translated 
    if native_language == 'FR':
        translated_french = 'NO'
        translated_english = 'YES'
    elif native_language == 'EN':
        translated_french = 'YES'
        translated_english = 'NO'
    elif native_language == 'Unknown': #if you don't know the native language, you can't know if its translated 
        translated_french = 'unknown'
        translated_english = 'unknown'
    else: #getting here means the native language is another EU language -- it will be translated for both english and french 
        translated_french = 'YES'
        translated_english = 'YES' 
    
    #make rows 
    data.append([native_language, 'FR', translated_french, french])
    data.append([native_language, 'EN', translated_english, english])

df = pd.DataFrame(data, columns=['native_language', 'utterance_language', 'translated', 'sentence'])
print(df)

#get some info about the corpus 
translated_count = (df['translated'] == 'YES').sum()
print("number of translated sentences: ", translated_count)
untranslated_count = (df['translated'] == 'NO').sum()
print("numer of untranslated sentences: ", untranslated_count)
unk_translated_count = (df['translated'] == 'unknown').sum()
print("number of sentences where we don't know if it's translated: ", unk_translated_count)

native_en_count = (df['native_language'] == 'EN').sum() 
print("number of native english sentences: ", native_en_count)
native_fr_count = (df['native_language'] == 'FR').sum() 
print("number of native french sentences: ", native_fr_count)
native_unk_count = (df['native_language'] == 'Unknown').sum() 
print("number of unknown native languages: ", native_unk_count) 

#save combined data into a .csv because that's the only thing i know how to read 
csv_name = 'europarl_corpus.csv'
df.to_csv(csv_name)