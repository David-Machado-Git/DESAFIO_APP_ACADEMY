from time import sleep


def lista_dados():
    dados = [{'nome': 'Ãgatha Almeida', 'vaga': 'QA', 'idade': '26 ', 'estado': 'SC' },
{'nome': 'Ãgatha Santos', 'vaga': 'Android', 'idade': '26 ', 'estado': 'SC' },
{'nome': 'Ãgatha Sousa', 'vaga': 'Android', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Ãgatha Souza', 'vaga': 'QA', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'Alex Santos', 'vaga': 'QA', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Alex Sousa', 'vaga': 'QA', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Alice Gomes', 'vaga': 'Android', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Alice Lima', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Aline Cunha', 'vaga': 'iOS', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Aline Fernandes', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Aline Martins', 'vaga': 'iOS', 'idade': '33 ', 'estado': 'SC' },
{'nome': 'Amanda Cardoso', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Amanda Pinto', 'vaga': 'Android', 'idade': '29 ', 'estado': 'SC' },
{'nome': 'Ana Castro', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Ana Correia', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'AndrÃ© Melo', 'vaga': 'Android', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'AndrÃ© Souza', 'vaga': 'iOS', 'idade': '26 ', 'estado': 'SC' },
{'nome': 'Anna Almeida', 'vaga': 'QA', 'idade': '26 ', 'estado': 'SC' },
{'nome': 'Anna Carvalho', 'vaga': 'QA', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'Anna Costa', 'vaga': 'Android', 'idade': '30 ', 'estado': 'GO' },
{'nome': 'Anna Costa', 'vaga': 'iOS', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Anna Santos', 'vaga': 'iOS', 'idade': '32 ', 'estado': 'SC' },
{'nome': 'AntÃ´nio Cavalcanti', 'vaga': 'Android', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'AntÃ´nio Ribeiro', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Arthur Barbosa', 'vaga': 'Android', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Arthur Cardoso', 'vaga': 'Android', 'idade': '29 ', 'estado': 'SP' },
{'nome': 'Arthur Fernandes', 'vaga': 'Android', 'idade': '26 ', 'estado': 'SC' },
{'nome': 'Arthur Goncalves', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Arthur Oliveira', 'vaga': 'QA', 'idade': '41 ', 'estado': 'SC' },
{'nome': 'Beatrice Araujo', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Beatrice Pereira', 'vaga': 'Android', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Beatriz Alves', 'vaga': 'iOS', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Beatriz Rodrigues', 'vaga': 'QA', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Bianca Azevedo', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Bianca Castro', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Bianca Cunha', 'vaga': 'Android', 'idade': '35 ', 'estado': 'SC' },
{'nome': 'Brenda Gomes', 'vaga': 'Android', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'Brenda Sousa', 'vaga': 'Android', 'idade': '50 ', 'estado': 'SC' },
{'nome': 'Breno Pereira', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Bruna Martins', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Caio Melo', 'vaga': 'Android', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'Camila Barros', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Camila Cardoso', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Camila Lima', 'vaga': 'QA', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Carla Barros', 'vaga': 'Android', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Carlos Martins', 'vaga': 'QA', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Carlos Martins', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Carolina Goncalves', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Carolina Sousa', 'vaga': 'QA', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Clara Lima', 'vaga': 'QA', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'Daniel Melo', 'vaga': 'iOS', 'idade': '55 ', 'estado': 'SC' },
{'nome': 'Daniel Pinto', 'vaga': 'Android', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Danilo Conrado', 'vaga': 'iOS', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Danilo Correia', 'vaga': 'QA', 'idade': '47 ', 'estado': 'SC' },
{'nome': 'Davi Barros', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Davi Ferreira', 'vaga': 'QA', 'idade': '33 ', 'estado': 'SC' },
{'nome': 'Diego Barbosa', 'vaga': 'iOS', 'idade': '25 ', 'estado': 'RJ' },
{'nome': 'Diego Castro', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Diego Pereira', 'vaga': 'Android', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Douglas Barros', 'vaga': 'QA', 'idade': '30 ', 'estado': 'SC' },
{'nome': 'Eduarda Barros', 'vaga': 'Android', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Eduarda Silva', 'vaga': 'iOS', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Eduardo Oliveira', 'vaga': 'Android', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Eduardo Souza', 'vaga': 'iOS', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Emilly Barros', 'vaga': 'Android', 'idade': '37 ', 'estado': 'SC' },
{'nome': 'Emilly Fernandes', 'vaga': 'Android', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Emilly Pereira', 'vaga': 'iOS', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Emilly Sousa', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SP' },
{'nome': 'Emily Cunha', 'vaga': 'QA', 'idade': '35 ', 'estado': 'SC' },
{'nome': 'Emily Ferreira', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Enzo Barros', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Enzo Barros', 'vaga': 'Android', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Erick Santos', 'vaga': 'QA', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Estevan Alves', 'vaga': 'Android', 'idade': '30 ', 'estado': 'PR' },
{'nome': 'Estevan Castro', 'vaga': 'Android', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'Estevan Cavalcanti', 'vaga': 'iOS', 'idade': '26 ', 'estado': 'SP' },
{'nome': 'Estevan Rocha', 'vaga': 'QA', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Estevan Rodrigues', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Evelyn Carvalho', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Evelyn Rodrigues', 'vaga': 'QA', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Felipe Fernandes', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SP' },
{'nome': 'Fernanda Almeida', 'vaga': 'QA', 'idade': '26 ', 'estado': 'SC' },
{'nome': 'Fernanda Barbosa', 'vaga': 'Android', 'idade': '31 ', 'estado': 'SC' },
{'nome': 'Fernanda Goncalves', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Fernanda Ribeiro', 'vaga': 'QA', 'idade': '46 ', 'estado': 'SC' },
{'nome': 'Fernanda Santos', 'vaga': 'QA', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Fernandu Vieira', 'vaga': 'QA', 'idade': '29 ', 'estado': 'SC' },
{'nome': 'Gabriel Costa', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Gabriela Correia', 'vaga': 'QA', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Gabrielle Costa', 'vaga': 'QA', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Gabrielle Rocha', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Gabrielle Rodrigues', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Gabrielly Azevedo', 'vaga': 'iOS', 'idade': '25 ', 'estado': 'SC' },
{'nome': 'Gabrielly Cardoso', 'vaga': 'QA', 'idade': '40 ', 'estado': 'SC' },
{'nome': 'Gabrielly Cunha', 'vaga': 'iOS', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Gabrielly Cunha', 'vaga': 'QA', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Giovanna Castro', 'vaga': 'QA', 'idade': '32 ', 'estado': 'SC' },
{'nome': 'Giovanna Costa', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Giovanna Cunha', 'vaga': 'QA', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Giovanna Silva', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Guilherme Oliveira', 'vaga': 'QA', 'idade': '30 ', 'estado': 'SP' },
{'nome': 'Guilherme Ribeiro', 'vaga': 'Android', 'idade': '29 ', 'estado': 'SC' },
{'nome': 'Gustavo Costa', 'vaga': 'QA', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Heitor Goncalves', 'vaga': 'QA', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'Igor Martins', 'vaga': 'QA', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Isabela Araujo', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Isabella Carvalho', 'vaga': 'iOS', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'Isabella Ribeiro', 'vaga': 'iOS', 'idade': '25 ', 'estado': 'SC' },
{'nome': 'Isabelle Cardoso', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Isabelle Dias', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Isabelle Ribeiro', 'vaga': 'iOS', 'idade': '38 ', 'estado': 'SC' },
{'nome': 'Isabelle Rocha', 'vaga': 'Android', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'JÃºlia Azevedo', 'vaga': 'iOS', 'idade': '35 ', 'estado': 'AM' },
{'nome': 'JÃºlio Fernandes', 'vaga': 'Android', 'idade': '26 ', 'estado': 'SC' },
{'nome': 'JoÃ£o Cunha', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'JoÃ£o Gomes', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'JosÃ© Goncalves', 'vaga': 'Android', 'idade': '30 ', 'estado': 'SC' },
{'nome': 'JosÃ© Santos', 'vaga': 'Android', 'idade': '27 ', 'estado': 'RJ' },
{'nome': 'JosÃ© Silva', 'vaga': 'QA', 'idade': '48 ', 'estado': 'SC' },
{'nome': 'Julia Castro', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Julian Cardoso', 'vaga': 'QA', 'idade': '40 ', 'estado': 'SC' },
{'nome': 'Julian Cardoso', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Julieta Pinto', 'vaga': 'Android', 'idade': '33 ', 'estado': 'SC' },
{'nome': 'Kai Carvalho', 'vaga': 'QA', 'idade': '25 ', 'estado': 'SC' },
{'nome': 'Kai Dias', 'vaga': 'Android', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Kaua Ferreira', 'vaga': 'iOS', 'idade': '26 ', 'estado': 'SP' },
{'nome': 'KauÃ£ Cardoso', 'vaga': 'QA', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'KauÃ£ Ferreira', 'vaga': 'iOS', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'KauÃª Araujo', 'vaga': 'QA', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'KauÃª Souza', 'vaga': 'QA', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Kauan Dias', 'vaga': 'iOS', 'idade': '29 ', 'estado': 'SC' },
{'nome': 'Kauan Ferreira', 'vaga': 'Android', 'idade': '30 ', 'estado': 'SC' },
{'nome': 'Kauan Martins', 'vaga': 'Android', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'Lara Fernandes', 'vaga': 'iOS', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Larissa Ribeiro', 'vaga': 'Android', 'idade': '25 ', 'estado': 'SP' },
{'nome': 'Leila Costa', 'vaga': 'iOS', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Leila Silva', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Leonardo Alves', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Leonardo Silva', 'vaga': 'iOS', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Leonor Gomes', 'vaga': 'Android', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'Leonor Oliveira', 'vaga': 'QA', 'idade': '32 ', 'estado': 'SC' },
{'nome': 'LetÃ­cia Ribeiro', 'vaga': 'Android', 'idade': '34 ', 'estado': 'SC' },
{'nome': 'Livia Araujo', 'vaga': 'iOS', 'idade': '39 ', 'estado': 'SC' },
{'nome': 'Livia Cunha', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Livia Rodrigues', 'vaga': 'iOS', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Luana Rodrigues', 'vaga': 'QA', 'idade': '29 ', 'estado': 'SC' },
{'nome': 'Luana Santos', 'vaga': 'Android', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'LuÃ­s Almeida', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'LuÃ­s Lima', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Lucas Araujo', 'vaga': 'Android', 'idade': '54 ', 'estado': 'SC' },
{'nome': 'Luis Dias', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Luiz Gomes', 'vaga': 'iOS', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Luiza Cunha', 'vaga': 'QA', 'idade': '21 ', 'estado': 'SP' },
{'nome': 'Manuela Dias', 'vaga': 'Android', 'idade': '35 ', 'estado': 'SC' },
{'nome': 'Manuela Gomes', 'vaga': 'QA', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Marcos Rodrigues', 'vaga': 'Android', 'idade': '33 ', 'estado': 'SC' },
{'nome': 'Marcos Souza', 'vaga': 'QA', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Maria Alves', 'vaga': 'QA', 'idade': '19 ', 'estado': 'SP' },
{'nome': 'Maria Ferreira', 'vaga': 'Android', 'idade': '26 ', 'estado': 'SC' },
{'nome': 'Maria Oliveira', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Mariana Oliveira', 'vaga': 'iOS', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'Mariana Rodrigues', 'vaga': 'Android', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Marina Costa', 'vaga': 'Android', 'idade': '34 ', 'estado': 'SC' },
{'nome': 'Marina Goncalves', 'vaga': 'QA', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'Marina Pinto', 'vaga': 'QA', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Marisa Cardoso', 'vaga': 'iOS', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Martim Almeida', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Martim Azevedo', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Mateus Silva', 'vaga': 'QA', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Matheus Alves', 'vaga': 'iOS', 'idade': '50 ', 'estado': 'SC' },
{'nome': 'Matheus Barbosa', 'vaga': 'iOS', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Matheus Carvalho', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Matilde Barros', 'vaga': 'Android', 'idade': '25 ', 'estado': 'SC' },
{'nome': 'Matilde Carvalho', 'vaga': 'QA', 'idade': '33 ', 'estado': 'SC' },
{'nome': 'Matilde Rodrigues', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Melissa Cunha', 'vaga': 'QA', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Miguel Correia', 'vaga': 'QA', 'idade': '29 ', 'estado': 'SC' },
{'nome': 'Miguel Fernandes', 'vaga': 'Android', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Miguel Rodrigues', 'vaga': 'QA', 'idade': '39 ', 'estado': 'SC' },
{'nome': 'Murilo Gomes', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Nicolas Almeida', 'vaga': 'QA', 'idade': '33 ', 'estado': 'SC' },
{'nome': 'Nicolas Araujo', 'vaga': 'iOS', 'idade': '28 ', 'estado': 'SP' },
{'nome': 'Nicolash Almeida', 'vaga': 'iOS', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Nicolash Cunha', 'vaga': 'QA', 'idade': '27 ', 'estado': 'SC' },
{'nome': 'Nicole Carvalho', 'vaga': 'QA', 'idade': '33 ', 'estado': 'SC' },
{'nome': 'Nicole Ferreira', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Nicole Sousa', 'vaga': 'Android', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'OtÃ¡vio Fernandes', 'vaga': 'QA', 'idade': '30 ', 'estado': 'SC' },
{'nome': 'OtÃ¡vio Ferreira', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Paulo Cunha', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Paulo Gomes', 'vaga': 'iOS', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Paulo Goncalves', 'vaga': 'Android', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Paulo Rocha', 'vaga': 'QA', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Pedro Barros', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Rafael Araujo', 'vaga': 'iOS', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Rafael Castro', 'vaga': 'Android', 'idade': '36 ', 'estado': 'SC' },
{'nome': 'Rafael Cavalcanti', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Rafael Costa', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Rafael Martins', 'vaga': 'QA', 'idade': '32 ', 'estado': 'SC' },
{'nome': 'Rafael Pinto', 'vaga': 'Android', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'Rafaela Cunha', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Raissa Ribeiro', 'vaga': 'Android', 'idade': '30 ', 'estado': 'SC' },
{'nome': 'Rebeca Araujo', 'vaga': 'iOS', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Renan Cunha', 'vaga': 'Android', 'idade': '22 ', 'estado': 'SC' },
{'nome': 'Renan Ferreira', 'vaga': 'QA', 'idade': '38 ', 'estado': 'SC' },
{'nome': 'Renan Goncalves', 'vaga': 'Android', 'idade': '21 ', 'estado': 'SC' },
{'nome': 'Rodrigo Carvalho', 'vaga': 'Android', 'idade': '24 ', 'estado': 'SC' },
{'nome': 'Ryan Barbosa', 'vaga': 'QA', 'idade': '17 ', 'estado': 'SC' },
{'nome': 'Ryan Souza', 'vaga': 'iOS', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Samuel Fernandes', 'vaga': 'Android', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Samuel Ribeiro', 'vaga': 'QA', 'idade': '25 ', 'estado': 'SC' },
{'nome': 'Sarah Rodrigues', 'vaga': 'QA', 'idade': '49 ', 'estado': 'SC' },
{'nome': 'Sofia Alves', 'vaga': 'QA', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'Sofia Rodrigues', 'vaga': 'iOS', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Sophia Correia', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'TÃ¢nia Rodrigues', 'vaga': 'Android', 'idade': '32 ', 'estado': 'SC' },
{'nome': 'ThaÃ­s Barbosa', 'vaga': 'QA', 'idade': '31 ', 'estado': 'SC' },
{'nome': 'ThaÃ­s Cavalcanti', 'vaga': 'QA', 'idade': '20 ', 'estado': 'AL' },
{'nome': 'Thiago Carvalho', 'vaga': 'Android', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Tiago Barros', 'vaga': 'QA', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'Tiago Oliveira', 'vaga': 'Android', 'idade': '30 ', 'estado': 'SC' },
{'nome': 'TomÃ¡s Cunha', 'vaga': 'QA', 'idade': '19 ', 'estado': 'SC' },
{'nome': 'Victor Cardoso', 'vaga': 'Android', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'VinÃ­cius Azevedo', 'vaga': 'QA', 'idade': '34 ', 'estado': 'SC' },
{'nome': 'VinÃ­cius Fernandes', 'vaga': 'iOS', 'idade': '28 ', 'estado': 'SC' },
{'nome': 'VitÃ³ria Dias', 'vaga': 'QA', 'idade': '20 ', 'estado': 'SC' },
{'nome': 'VitÃ³ria Fernandes', 'vaga': 'QA', 'idade': '18 ', 'estado': 'SC' },
{'nome': 'Vitor Costa', 'vaga': 'Android', 'idade': '23 ', 'estado': 'SC' },
{'nome': 'Vitor Gomes', 'vaga': 'QA', 'idade': '42 ', 'estado': 'SC' },
{'nome': 'Yasmin Dias', 'vaga': 'Android', 'idade': '21 ', 'estado': 'SC' }]

    return dados

tot_cadastrados = len(lista_dados())
contador_menu_1 = 0
contador = 0
contador_qa = 0
contador_android = 0
contador_ios = 0
tot_idade_candidatos_qa = int(0)
contador_estado_sc = 0
contador_estado_sp = 0
contador_estado_pr = 0
contador_estado_rj = 0
contador_estado_am = 0
contador_estado_al = 0
contador_estado_go = 0
estado_novo = []
contador_estado_distinto = 0


print('--' * 35)
print(f'\033[7;40m{"   ESTATÍSTICA DE DADOS  ":*^70}\033[0;0m')
print('--' * 35)

while True:
    print(f'     |-- {"OPÇÃO  ":-<2}{"   MENU   ":-^38}            |')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print(f'     |\033[1;30m\033[1;43m{" -> 1 <-":.<3}|{" - VISUALIZAR TODOS DADOS CADASTRADOS ":^38}             \033[0;0m|')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print(f'     |{" -> 2 <-":.<3}|{"  - IDADE MÉDIA DOS CANDIDATOS QA - ":^38}             |')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print(f'     |\033[1;30m\033[1;43m{" -> 3 <-":.<3}|{" - NÚMEROS ESTADOS DISTINTOS NA LISTA - ":^38}           \033[0;0m|')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print(f'     |{" -> 4 <-":.<3}|{" - ESTADO COM MENAS OCORRÊNCIAS - ":^38}             |')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print('--' * 35)
    print(f'\033[7;40m{"   ESCOLHA UMA DAS OPÇÕES ACIMA:  ":*^70}\033[0;0m')
    print('--' * 35)

    opcao_menu = str(input('Digite a opção desejada:?'))


    if opcao_menu.isnumeric():

        if opcao_menu == '1':

            print('--' * 35)
            print('        \033[1;40m    AGUARDE ! CARREGANDO LISTA\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m50%\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m100%\033[0;0m', end='')
            print('\033[1;40m   \033[0;0m', end='')
            print('\n')

            print('--' * 35)
            print(f'\033[7;40m{"   LISTANDO CLIENTES  ":*^70}\033[0;0m')
            print('--' * 35)

            while contador_menu_1 < len(lista_dados()):  # --> LAÇO QUE MOSTRA OS DADOS:
                print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
                print(f' {contador_menu_1+1} --> | {lista_dados()[contador_menu_1]["nome"]} {lista_dados()[contador_menu_1]["idade"]} anos, reside em: {lista_dados()[contador_menu_1]["estado"]} -- vaga: {lista_dados()[contador_menu_1]["vaga"]} ')
                contador_menu_1 += 1

            print(f'-------------------------------------------------------------------------  ')
            print('\033[1;90m    ----------------------- / FINAL LISTA / -----------------------\033[0;0m')
            print('--' * 30)
            print()
            print()

            while True:
                voltar_menu_principal = str(input('Digite:[S]-SAIR:')).strip().upper()[0]
                if voltar_menu_principal == 'S':
                    break

                else:
                    print(f'\033[1;41mSOMENTE DIGITE A LETRA [S]-PARA SAIR! :\033[0;0m')

            print('--' * 35)
            print('             \033[1;30m\033[1;43m     CARREGANDO MENU PRINCIPAL\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m50%\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m100%\033[0;0m', end='')
            print('\033[1;30m\033[1;43m   \033[0;0m', end='')
            print('\n')

            contador_menu_1 = 0





        elif opcao_menu == '2':

            print('--' * 35)
            print('        \033[1;40m    AGUARDE ! BUSCANDO INFORMAÇÕES\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m50%\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m100%\033[0;0m', end='')
            print('\033[1;40m   \033[0;0m', end='')
            print('\n')

            print('--' * 35)
            print(f'\033[7;40m{"   IDADE MÉDIA DOS CANDIDATOS QA  ":*^70}\033[0;0m')
            print('--' * 35)

            while contador < len(lista_dados()):
                if lista_dados()[contador]["vaga"] == 'QA':
                    contador_qa += 1
                    idade_candidato_qa = int(lista_dados()[contador]["idade"])
                    tot_idade_candidatos_qa += idade_candidato_qa
                    # print(f'Idade individual é: {idade_candidato_qa}')
                    # print(f'{contador_qa} --> idade {tot_idade_candidatos_qa}')
                contador += 1

            idade_media_candidatos_qa = tot_idade_candidatos_qa / contador_qa
            print()
            print()
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print(f'A idade media dos candidatos de QA é: {idade_media_candidatos_qa:.2f}')
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print()
            print()
            print()
            while True:
                voltar_menu_principal = str(input('Digite:[S]-SAIR:')).strip().upper()[0]
                if voltar_menu_principal == 'S':
                    break

                else:
                    print(f'\033[1;41mSOMENTE DIGITE A LETRA [S]-PARA SAIR! :\033[0;0m')

            print('--' * 35)
            print('             \033[1;30m\033[1;43m     CARREGANDO MENU PRINCIPAL\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m50%\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m100%\033[0;0m', end='')
            print('\033[1;30m\033[1;43m   \033[0;0m', end='')
            print('\n')

            contador = 0



        elif opcao_menu == '3':

            print('--' * 35)
            print('        \033[1;40m    AGUARDE ! BUSCANDO INFORMAÇÕES\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m50%\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m100%\033[0;0m', end='')
            print('\033[1;40m   \033[0;0m', end='')
            print('\n')

            print('--' * 35)
            print(f'\033[7;40m{"   NÚMEROS ESTADOS DISTINTOS PRESENTES NA LISTA  ":*^70}\033[0;0m')
            print('--' * 35)
            while contador < len(lista_dados()):
                # if contador == 0:
                #
                #     estado_novo.append(lista_dados()[contador]["estado"])
                #     quantida_estado_novo = int(len(estado_novo))
                    # print(f'{lista_dados()[contador]["estado"]}')



                if contador >= 0 and lista_dados()[contador]["estado"] in estado_novo:
                    var = 'analise_dados'

                else:
                    estado_novo.append(lista_dados()[contador]["estado"])
                    contador_estado_distinto += 1

                contador += 1



            print()
            print()
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print(f'Ao todo são: {contador_estado_distinto} estados distintos presentes na lista:')
            print(f'sendo eles: {estado_novo}')
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print()
            print()
            print()
            while True:
                voltar_menu_principal = str(input('Digite:[S]-SAIR:')).strip().upper()[0]
                if voltar_menu_principal == 'S':
                    break

                else:
                    print(f'\033[1;41mSOMENTE DIGITE A LETRA [S]-PARA SAIR! :\033[0;0m')

            print('--' * 35)
            print('             \033[1;30m\033[1;43m     CARREGANDO MENU PRINCIPAL\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m50%\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m100%\033[0;0m', end='')
            print('\033[1;30m\033[1;43m   \033[0;0m', end='')
            print('\n')

            contador = 0


        elif opcao_menu == '4':
            print('--' * 35)
            print('        \033[1;40m    AGUARDE ! BUSCANDO INFORMAÇÕES\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;40m50%\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;40m100%\033[0;0m', end='')
            print('\033[1;40m   \033[0;0m', end='')
            print('\n')

            print('--' * 35)
            print(f'\033[7;40m{"   ESTADO COM MENAS OCORRÊNCIAS  ":*^70}\033[0;0m')
            print('--' * 35)

            while contador < len(lista_dados()):
                if lista_dados()[contador]["vaga"] == 'QA':
                    contador_qa += 1
                    idade_candidato_qa = int(lista_dados()[contador]["idade"])
                    tot_idade_candidatos_qa += idade_candidato_qa


                elif lista_dados()[contador]["vaga"] == 'Android':
                    contador_android += 1

                elif lista_dados()[contador]["vaga"] == 'iOS':
                    contador_ios += 1

                if lista_dados()[contador]["estado"] == 'SC':
                    contador_estado_sc += 1

                elif lista_dados()[contador]["estado"] == 'SP':
                    contador_estado_sp += 1

                elif lista_dados()[contador]["estado"] == 'PR':
                    contador_estado_pr += 1
                    nome_candidato_pr = lista_dados()[contador]["nome"]
                    idade_candidato_pr = lista_dados()[contador]["idade"]
                    estado_pessoa_pr = lista_dados()[contador]["estado"]
                    vaga_pessoa_pr = lista_dados()[contador]["vaga"]

                elif lista_dados()[contador]["estado"] == 'RJ':
                    contador_estado_rj += 1
                    if contador_estado_rj == 1:
                        um_nome_candidato_rj = lista_dados()[contador]["nome"]
                        um_idade_candidato_rj = lista_dados()[contador]["idade"]
                        um_estado_pessoa_rj = lista_dados()[contador]["estado"]
                        um_vaga_pessoa_rj = lista_dados()[contador]["vaga"]

                    elif contador_estado_rj == 2:
                        dois_nome_candidato_rj = lista_dados()[contador]["nome"]
                        dois_idade_candidato_rj = lista_dados()[contador]["idade"]
                        dois_estado_pessoa_rj = lista_dados()[contador]["estado"]
                        dois_vaga_pessoa_rj = lista_dados()[contador]["vaga"]

                elif lista_dados()[contador]["estado"] == 'AM':
                    contador_estado_am += 1
                    nome_candidato_am = lista_dados()[contador]["nome"]
                    idade_candidato_am = lista_dados()[contador]["idade"]
                    estado_pessoa_am = lista_dados()[contador]["estado"]
                    vaga_pessoa_am = lista_dados()[contador]["vaga"]

                elif lista_dados()[contador]["estado"] == 'AL':
                    contador_estado_al += 1
                    nome_candidato_al = lista_dados()[contador]["nome"]
                    idade_candidato_al = lista_dados()[contador]["idade"]
                    estado_pessoa_al = lista_dados()[contador]["estado"]
                    vaga_pessoa_al = lista_dados()[contador]["vaga"]

                elif lista_dados()[contador]["estado"] == 'GO':
                    contador_estado_go += 1
                    nome_candidato_go = lista_dados()[contador]["nome"]
                    idade_candidato_go = lista_dados()[contador]["idade"]
                    estado_pessoa_go = lista_dados()[contador]["estado"]
                    vaga_pessoa_go = lista_dados()[contador]["vaga"]

                if contador > -1:
                    n_ocorrencia = contador + 1
                    convertendo_idade_str_int = int(lista_dados()[contador]["idade"])
                    # print(f'{n_ocorrencia} - Teste fatiamento dados instrutor: {convertendo_idade_str_int}')

                    if convertendo_idade_str_int < 31 and lista_dados()[contador]["estado"] == 'SC':
                        loading = 'carregando'
                        # print(f'{n_ocorrencia} - {lista_dados()[contador]}')

                contador += 1

            print('Abaixo seguem os dados das pessoas nos estados com menas ocorrências:')
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print()
            print()
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print('No Paraná temos:')
            print(f'Nome: {nome_candidato_pr} / Idade:{idade_candidato_pr} / Estado:{estado_pessoa_pr} / Vaga:{vaga_pessoa_pr}')
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print('EM RJ:')
            print(f'Nome: {um_nome_candidato_rj} / Idade:{um_idade_candidato_rj} / Estado:{um_estado_pessoa_rj} / Vaga:{um_vaga_pessoa_rj}')
            print(f'Nome: {dois_nome_candidato_rj} / Idade:{dois_idade_candidato_rj} / Estado:{dois_estado_pessoa_rj} / Vaga:{dois_vaga_pessoa_rj}')
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print('EM GO:')
            print(f'Nome: {nome_candidato_go} / Idade:{idade_candidato_go} / Estado:{estado_pessoa_go} / Vaga:{vaga_pessoa_go}')
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print('EM AM:')
            print(f'Nome: {nome_candidato_am} / Idade:{idade_candidato_am} / Estado:{estado_pessoa_am} / Vaga:{vaga_pessoa_am}')
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print('EM AL:')
            print(f'Nome: {nome_candidato_al} / Idade:{idade_candidato_al} / Estado:{estado_pessoa_al} / Vaga:{vaga_pessoa_al}')
            print(f'\033[1;90m-------------------------------------------------------------------------|  \033[0;0m')
            print(f'')

            while True:
                voltar_menu_principal = str(input('Digite:[S]-SAIR:')).strip().upper()[0]
                if voltar_menu_principal == 'S':
                    break

                else:
                    print(f'\033[1;41mSOMENTE DIGITE A LETRA [S]-PARA SAIR! :\033[0;0m')

            print('--' * 35)
            print('             \033[1;30m\033[1;43m     CARREGANDO MENU PRINCIPAL\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.3)
            print('\033[1;30m\033[1;43m50%\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m.\033[0;0m', end='')
            sleep(0.8)
            print('\033[1;30m\033[1;43m100%\033[0;0m', end='')
            print('\033[1;30m\033[1;43m   \033[0;0m', end='')
            print('\n')

            contador = 0



