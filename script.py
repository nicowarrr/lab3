import sys

def transform_and_save(input_file, output_file):
    def transform_line(line):
        if line and line[0].isalpha():
            return line[0].upper() + line[1:] + "0"
        elif line and line[0].isdigit():
            return ""
        else:
            return line

    line_count = 0

    try:
        with open(input_file, "r", encoding="ISO-8859-1") as infile, open(output_file, "w") as outfile:
            for line in infile:
                transformed_line = transform_line(line.strip())
                if transformed_line:
                    outfile.write(transformed_line + "\n")
                    line_count += 1
        print(f"Transformación completada. Resultado guardado en '{output_file}'.")
        print(f"Líneas procesadas: {line_count}")
    except FileNotFoundError:
        print(f"El archivo '{input_file}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python programa.py nombre_del_archivo entrada nombre_del_archivo salida")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    transform_and_save(input_file, output_file)
