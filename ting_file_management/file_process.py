from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    list_of_paths = list()
    list_of_files = dict()

    for index in range(len(instance)):
        list_of_paths.append(instance.search(index))

    if path_file not in list_of_paths:
        file = txt_importer(path_file)

        list_of_files["nome_do_arquivo"] = path_file
        list_of_files["qtd_linhas"] = len(file)
        list_of_files["linhas_do_arquivo"] = file

    instance.enqueue(list_of_files)
    sys.stdout.write(str(list_of_files))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")

    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        files = instance.search(position)
        sys.stdout.write(str(files))
    except IndexError:
        sys.stderr.write("Posição inválida")
