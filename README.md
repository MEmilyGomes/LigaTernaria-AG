<div align="center">
  <img src="Imagens/logo_Ilum-CNPEM.png" alt="Descrição da imagem" width="1000"/>
</div>

<h1 align="center">A liga ternária leve mais cara do mundo ⛓️:</h1>
<h2 align="center">Encontrando com algoritmo genético</h2>

<p align="center"><strong>Autoras:</strong> Ana Luz Pereira Mendes e Maria Emily Nayla Gomes da Silva</p>
<p align="center"><strong>Orientador:</strong> Prof. Dr. Daniel R. Cassar</p>


<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>


## 📝 Descrição
<p align="justify">
Este projeto tem como objetivo encontrar a liga ternária leve de maior custo. Ou seja, queremos identificar, por meio de algoritmo genético, uma combinação de três elementos em que o código minimize o peso atômico e maximize o valor da liga. Diante disso, transformamos o problema multiobjetivo em um problema monoobjetivo ao considerar que os melhores indivíduos são aqueles que maximizam a diferença entre o valor da liga e seu peso molecular. Construímos os indivíduos de forma que os três primeiros genes representem os elementos presentes na liga, e os três últimos, as massas associadas a cada elemento. Assim, um indivíduo é representado como: <code>[Elemento1, Elemento2, Elemento3, Peso1, Peso2, Peso3]</code>. Além disso, consideramos a restrição de no mínimo 5 gramas para cada elemento.
</p>

## 📔 Notebooks e arquivos do projeto
* `Imagens/logo_Ilum-CNPEM.png` — Imagem da instituição Ilum - CNPEM.  
* `funcoes_liga.py` — Script com as funções utilizadas no projeto de ligas ternárias.  
* `ligaternaria.ipynb` — Notebook principal do projeto de ligas ternárias.

## 🪼 Funções adaptadas para o problema das ligas ternárias

### <code>Função Objetivo</code>  
<p align="justify">
Para computar o fitness dos indivíduos, definiu-se que seria calculada a diferença entre o valor da liga e seu peso molecular, pois desejamos o maior valor possível e o menor peso atômico. Assim, quanto maior a diferença, melhor o desempenho do indivíduo — atendendo ao objetivo de maximizar o valor e minimizar o peso molecular.
</p>

### <code>Cruzamento</code>  
<p align="justify">
Nessa etapa, optamos por cruzar apenas a parte dos elementos do candidato, ou seja, os três primeiros genes. Isso porque, com a restrição do peso máximo, cruzar também os pesos poderia gerar muitos indivíduos inválidos.
</p>

### <code>Mutação da Massa</code>  
<p align="justify">
Para realizar essa mutação, sorteamos um dos pesos para mantê-lo fixo. Em seguida, sorteamos um segundo peso entre 5g e o valor máximo permitido, desconsiderando o peso já fixado. Com esses dois valores definidos, o terceiro peso é calculado de forma que a soma total continue respeitando as restrições do problema.
</p>

### <code>Mutação do Elemento</code>  
<p align="justify">
Para realizar essa mutação, sorteia-se um dos três elementos da liga para ser alterado. Em seguida, escolhe-se aleatoriamente um novo elemento possível — exceto aqueles que já estão presentes no indivíduo — garantindo, assim, a criação de um indivíduo válido.
</p>

## 😁 Conclusão
<p align="justify">
Portanto, neste notebook foi possível implementar um código de algoritmo genético que resolve o problema das ligas ternárias — em que se deseja aumentar o valor da liga e diminuir o peso molecular. Um desafio do projeto foi identificar como seria calculado o fitness, já que a ordem de grandeza entre as massas, assim como entre os valores por quilograma dos elementos, varia drasticamente. Contudo, consideramos que obtivemos um excelente resultado, visto que o código convergiu para ligas compostas por elementos de altíssimo valor associado e massas que, embora não sejam as menores, também não estão muito distantes da massa de outros elementos. </p>

## 🖇️ Informações técnicas
* Linguagem de programação: `Python 3.9`
* Software:  `Jupyter Notebook`
* **Bibliotecas e Módulos:** `random`

## 🧠 Contribuições dos Colaboradores
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/172425049?v=4" width=115><br><sub>Ana Luz Pereira Mendes</sub>](https://github.com/LuzMendes)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](https://lattes.cnpq.br/4596466138573531) [<sub>Linkedin</sub>](https://www.linkedin.com/in/ana-luz-pereira-mendes/)| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/172424897?v=4" width=115><br><sub> Maria Emily Nayla</sub>](https://github.com/MEmilyGomes)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](http://lattes.cnpq.br/9482558334105708)<br> | [<img loading="lazy" src="https://github.com/user-attachments/assets/463d4753-7fa4-4a42-aa54-409e4150bb51" width=115><br> <sub> Prof. Dr. Daniel R. Cassar </sub>](https://github.com/drcassar)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](http://lattes.cnpq.br/1717397276752482) | 
| :---: | :---: | :---: | 


#### Para o Projeto:
* **Ana Luz**: Implementação das funções para criar a população, cruzamento e mutação de massas, além da escrita do notebook.  
* **Emily Gomes**: Implementação das funções objetivo e de mutação de elemento, além da escrita do notebook.

#### Para o Repositório GitHub:
* **Ana Luz**: Upload do notebook principal.  
* **Emily Gomes**: README e upload do script.

**Orientação:** Prof. Dr. Daniel R. Cassar.
