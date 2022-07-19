def exists_word(word, instance):
    list_of_searchs = list()

    for index in range(len(instance)):
        file = instance.search(index)
        total_lines = file["linhas_do_arquivo"]
        line_counting = list()

# Ref: https://stackoverflow.com/questions/319426/
# how-do-i-do-a-case-insensitive-string-comparison
        for line in range(len(total_lines)):
            if word.lower() in total_lines[line].lower():
                line_counting.append({"linha": line + 1})

        if len(line_counting) > 0:
            list_of_searchs.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": line_counting,
            })

    return list_of_searchs


def search_by_word(word, instance):
    list_of_searchs = list()

    for index in range(len(instance)):
        file = instance.search(index)
        total_lines = file["linhas_do_arquivo"]
        line_counting = list()

        for line in range(len(total_lines)):
            if word.lower() in total_lines[line].lower():
                line_counting.append({
                    "linha": line + 1,
                    "conteudo": total_lines[line]
                })

        if len(line_counting) > 0:
            list_of_searchs.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": line_counting,
            })

    return list_of_searchs
