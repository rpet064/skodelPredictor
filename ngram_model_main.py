def create_ngram_model(n, path):
    m = NgramModel(n)
    with open(path, 'r') as f:
        text = f.read()
        text = text.split('.')
        for sentence in text:
            # add back the fullstop
            sentence += '.'
            m.update(sentence)
    return m



if __name__ == "__main__":
    start = time.time()
    m = create_ngram_model(3, 'Frankenstein.txt')

    print (f'Language Model creating time: {time.time() - start}')
    start = time.time()
    random.seed(5)
    
    print(f'{"="*50}\nGenerated text:')
    print(m.generate_text(20))
    print(f'{"="*50}')