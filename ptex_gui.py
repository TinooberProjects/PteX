
# #zona de imports
from cProfile import label
import tkinter as tk
from tkinter import ttk
from tkinter.constants import DISABLED

import tkinter.filedialog
from tkinter import Toplevel, messagebox
from tkinter.ttk import *


#bibliteca para importar e manipular as tabelas
#import pandas as pd

import subprocess
#bibliotecas para controlar o tempo e configuração de url
import time
import urllib










# ############################################################################################
def formulario():
        #título da janela
    # newWindow = Toplevel(janela)

    
    # newWindow = tk.Tk()
    newWindow = Toplevel(janela)
    newWindow.title("Construção da pasta do PTeX")
    newWindow.geometry("260x180")
    newWindow.config(bg="gray")
    newWindow.resizable(False,False)

   

    Label(newWindow,text ="Titulo").grid(row=1,column=1, sticky="NESW")



    titulo=tk.Entry(newWindow)
    titulo.grid(row=1,column=2, sticky="NESW")

    
    
    ########################################################

    Label(newWindow,text ="Autor").grid(row=2,column=1, sticky="NESW")



    autor=tk.Entry(newWindow)
    autor.grid(row=2,column=2, sticky="NESW")
    
###############################################################



    ########################################################

    Label(newWindow,text ="Local").grid(row=3,column=1, sticky="NESW")
   


    Local=tk.Entry(newWindow)
    Local.grid(row=3,column=2, sticky="NESW")

###############################################################
    ########################################################

    Label(newWindow,text ="Data").grid(row=4,column=1, sticky="NESW")



    data=tk.Entry(newWindow)
    data.grid(row=4,column=2, sticky="NESW")

###############################################################


    ########################################################

    Label(newWindow,text ="Orientador(a)").grid(row=5,column=1, sticky="NESW")



    orientador=tk.Entry(newWindow)
    orientador.grid(row=5,column=2, sticky="NESW")

###############################################################





    ########################################################

    Label(newWindow,text ="Data de Aprovação").grid(row=6,column=1, sticky="NESW")
  


    dataaprovacao=tk.Entry(newWindow)
    dataaprovacao.grid(row=6,column=2, sticky="NESW")
  
###############################################################



    ########################################################
  # 
    Label(newWindow,text ="Instituição").grid(row=7,column=1, sticky="NESW")



    instituicao=tk.Entry(newWindow)
    instituicao.grid(row=7,column=2, sticky="NESW")
    # 
###############################################################




    ########################################################
  # 
    Label(newWindow,text ="Curso").grid(row=8,column=1, sticky="NESW")
   


    curso=tk.Entry(newWindow)
    curso.grid(row=8,column=2, sticky="NESW")
    # 
###############################################################

 

    def gerar():
      tx_titulo=titulo.get()
      tx_autor=autor.get()
      tx_local=Local.get()
      tx_data=data.get()
      tx_orientador=orientador.get()
      tx_dataaprovacao=dataaprovacao.get()
      tx_instituicao=instituicao.get()
      tx_curso=curso.get()

      gerar_template(tx_titulo,tx_autor,tx_local,tx_data,tx_orientador,tx_dataaprovacao,tx_instituicao,tx_curso)
      

    Button(newWindow,text="Gerar",command=gerar).grid(row=9,columnspan=3,sticky="NESW")

   
    
     




############################################################################################

############################################## Funções ###########################################################################

def mostrar_manual():

     messagebox.showinfo("Ptex ver 1.0","Em Construção!")
#####################################################################################################
def gerar_template(titulo,autor,local,data,orientador,dataparovacao,instituicao,curso):
    
    
    # print("Titulo:{}, Autor:{}, local:{}, data:{},{} {} {} {}".format(titulo,autor,local,data,orientador,dataparovacao,instituicao,curso))
 
    
    arquivo = tkinter.filedialog.askdirectory(title="Selecione o local")
    

    referencias =r'''
@ABNT-options{minhasopcoes,
abnt-emphasize="\textbf",
}
        '''
    
    citacoes =r""" 
    
%AutorEvertonSantos 
%Pacoteadaptadodoabntex2 
 
\ProvidesPackage{citacao}
 
%%%modelo 
    
    
    """
    with open(arquivo+"/citacao.sty","a") as citacao:
        citacao.write(citacoes)
    citacao.close

    
    
    with open(arquivo+"/bibliografia.bib","a") as bibliografia:
        bibliografia.write(referencias)
    bibliografia.close

    ifba=r"""
 %Autor Everton Santos 
 %2022
 %Pacote adaptado do abntex2 
 


\ProvidesPackage{ptex}
%%%pacotes importados%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \usepackage[utf8]{inputenc} %pacote para inserir letras sem restrição
\usepackage{citacao}
\usepackage{graphicx,color,graphics} %pacote para inserir cores e gráficos
% \usepackage{subfigure}

\usepackage{indentfirst} % indenta a primeira linha do parágrafo

% \usepackage[alf,abnt-emphasize=bf]{abntex2cite} %citações pela abnt

\usepackage{pdfpages} %pacote para inserir pdf

\usepackage{hyperref}% pacote para inseir hiperlinks


%\usepackage{listadecitacoes}% A depender deletar
			
\usepackage[T1]{fontenc}
\usepackage{times}		% Selecao de codigos de fonte (times).
\usepackage[utf8]{inputenc}		% Codificacao do documento (conversão automática dos acentos)
\usepackage{lastpage}			% Usado pela Ficha catalográfica


\usepackage{microtype} 			% para melhorias de justificação
\usepackage{lastpage}
\usepackage{makeidx}        % indice Remissivo
% ---
	


\usepackage{caption}
\usepackage{subcaption}
\usepackage{float}




% ---
% Pacotes adicionais, usados apenas no âmbito do Modelo Canônico do abnteX2
% ---
\usepackage{lipsum}				% para geração de dummy text
% ---

% ---
% Pacotes de citações
% ---
\usepackage[brazilian,hyperpageref]{backref}	 % Paginas com as citações na bibl
\usepackage[alf, versalete, abnt-emphasize = bf, % destaca o titulo da revista ou livro em negrito;
abnt-etal-list = 3, % trabalhos com mais de 3 autores recebem et al.,;
abnt-etal-text = it, % escreve o et al., em italico;
abnt-and-type = &, % usa o carater '&' no lugar de 'e' para mais de um autor;
abnt-last-names = abnt, % trata sobrenomes 'estritamente' conforme a ABNT; e
abnt-repeated-author-omit = no % autores com + de uma entrada recebem '____.'
]{abntex2cite}	% Citações padrão ABNT
\usepackage{tocloft} %modifica o sumario




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%CONFIGURANDO AS FONTES fonte times %%%%%%%%%%%%%%%%%%%%%%%



\renewcommand{\ABNTEXchapterfont}{\fontfamily{ptm}\fontseries{b}\selectfont}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




\renewcommand{\baselinestretch}{1.5}  %espaçamanento entre linhas



% --- 
% CONFIGURAÇÕES DE PACOTES

% ---
% Configurações do pacote backref
% Usado sem a opção hyperpageref de backref
\renewcommand{\backrefpagesname}{Citado na(s) página(s):~}
% Texto padrão antes do número das páginas
\renewcommand{\backref}{}
% Define os textos da citação
\renewcommand*{\backrefalt}[4]{
	\ifcase #1 %
		Nenhuma citação no texto.%
	\or
		Citado na página #2.%
	\else
		Citado #1 vezes nas páginas #2.%
	\fi}%
% ---






%%%%%%%%%%%%%%%%%%%%%%%% espaçamento e margens %%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Espaçamentos entre linhas e parágrafos 
% O tamanho do parágrafo é dado por:



\setlrmarginsandblock{2.5cm}{2cm}{*} % externa/interna esquerda2.5 / direita2
\setulmarginsandblock{2.5cm}{2cm}{*} %superior2.5/inferior2
\checkandfixthelayout[fixed]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%numeracao com abntex2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\numeracao}[1]{\pagestyle{headings}\markboth{}{}}%comando para a numeracao certa
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%comando escrever artigo %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\escreverartigo}{\counterwithout{section}{section}}%comando para escrever artigo
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



 %%%%%%%%%%%%comando inicio e fim %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\inicio}{\begin{document}}%comando traduz o begin

  \newcommand{\fim}{\end{document}}%comando traduz o end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%% Estilizando o sumário %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    \renewcommand{\cftchapterfont}{\normalfont} % Tirar negrito das secoes no sumario
    \renewcommand{\cftsectionfont}{\normalfont} % Tirar negrito das secoes no sumario

\renewcommand{\cftsubsectionfont}{\normalfont} % Tirar negrito das subsecoes no sumario

\renewcommand{\cftsubsubsectionfont}{\normalfont} % Tirar negrito das subsubsecoes no sumario


\renewcommand{\ABNTEXchapterfontsize}{\normalsize}
\renewcommand{\ABNTEXsectionfontsize}{\normalsize}

\renewcommand{\ABNTEXsubsectionfontsize}{\normalsize}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%sumario %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\sumario}{ 

\newpage
\thispagestyle{empty} %limpa o estilo de formatação da página

  
 \begin{center}
  \cftsetindents{chapter}{10cm}{0cm}

% \cftsetindents{section}{0cm}{0.75cm}
% \cftsetindents{subsection}{0cm}{1cm}

\renewcommand{\contentsname}{Sumário} %renomeando o comando para sumario
\tableofcontents*   % a pagina de sumario nao e inserida no sumario
 
\end{center}  

\newpage % forca apos o sumario ele abrir uma nova pagina
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%% Figura%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%  H	Place exactly at spot in source text
%  h	Place approximately at spot in source test
%  t	Place at top of page
%  b	Place at bottom of page
%  p	Place on page for floats only
%  !	Override internal LaTeX parameters for determining float position




\providecommand{\usarnomefigura}{} % comando para inserir figura
\newcommand{\nomefigura}[1]{\renewcommand{\usarnomefigura}{#1}}
\providecommand{\usartamanhofigura}{} % comando para inserir figura
 \newcommand{\tamanhodafigura}[1]{\renewcommand{\usartamanhofigura}{#1}}

 \providecommand{\referenciar}{} % comando para inserir figura
 \newcommand{\apelidoimagem}[1]{\renewcommand{\referenciar}{#1}}

 \providecommand{\referenciardois}{} % comando para inserir figura
 \newcommand{\apelidoimagemum}[1]{\renewcommand{\referenciardois}{#1}}

 \providecommand{\referenciartres}{} % comando para inserir figura
 \newcommand{\apelidoimagemdois}[1]{\renewcommand{\referenciartres}{#1}}




 \providecommand{\usardescricaoimagem}{} % comando para inserir figura
 \newcommand{\descricaoimagem}[1]{\renewcommand{\usardescricaoimagem}{#1}}




 \providecommand{\usardescricaoimagemdois}{} % comando para inserir figura
 \newcommand{\descricaoimagemdois}[1]{\renewcommand{\usardescricaoimagemdois}{#1}}


 \providecommand{\usardescricaoimagemtres}{} % comando para inserir figura
 \newcommand{\descricaoimagemtres}[1]{\renewcommand{\usardescricaoimagemtres}{#1}}

 \providecommand{\usarlegendaimagem}{} % comando para inserir figura
 \newcommand{\legendaimagem}[1]{\renewcommand{\usarlegendaimagem}{#1}}

 \providecommand{\usarnomefiguradois}{} % comando para inserir figura
\newcommand{\nomefiguradois}[1]{\renewcommand{\usarnomefiguradois}{#1}}

 \newcommand{\inserirfigura}{
 \begin{figure}[H]
 \centering
  \caption{\label{\referenciar}\usardescricaoimagem}
  \vspace*{-0.2cm}
\includegraphics[scale=0.75]{\usarnomefigura}
 \vspace*{0cm}
 \legend{Fonte: \usarlegendaimagem}
 \end{figure}

}

\newcommand{\inserirfiguras}{
  \begin{figure}[H]
  \centering
   \caption{\label{\referenciar}\usardescricaoimagem}
   \vspace*{-0.2cm}
 \includegraphics[width=0.4\textwidth]{\usarnomefigura} \ \ \ \ \ \ \
 \includegraphics[width=0.4\textwidth]{\usarnomefiguradois}
  \vspace*{0cm}
  \legend{Fonte: \usarlegendaimagem}
  \end{figure}
 
 }


 \newcommand{\subfiguras}{
  \begin{figure}[H]
  \centering
   \caption{\usardescricaoimagem}
   \vspace*{-0.2cm}
   \begin{subfigure}{.4\textwidth}
		\includegraphics[width=\textwidth]{\usarnomefigura}
		\caption{\usardescricaoimagemdois}
    \label{\referenciardois}
	\end{subfigure}
  %%%%%%%%%%%%%%%%%%%
  \begin{subfigure}{.4\textwidth}
		\includegraphics[width=\textwidth]{\usarnomefiguradois}
		\caption{\label{\referenciartres}\usardescricaoimagemtres}
	\end{subfigure}
  \vspace*{0cm}
  \legend{Fonte: \usarlegendaimagem}
  \end{figure}
 
 }


%  \begin{figure}[H]
% 	\centering
% 	\begin{subfigure}{.3\textwidth}
% 		\includegraphics[width=\textwidth]{atom.png}
% 		\caption{Atom 1}
% 	\end{subfigure}
% %%%%%%%%%%%%%%
% 	\begin{subfigure}{.3\textwidth}
% 		\includegraphics[width=\textwidth]{atom.png}
% 		\caption{Atom 2}
% 	\end{subfigure}
% %%%%%%%%%%%%%%
% 	\begin{subfigure}{.3\textwidth}
% 		\includegraphics[width=\textwidth]{atom.png}
% 		\caption{Atom 3}
% 	\end{subfigure}
% 	\caption{Atoms are fun!}
% \end{figure}


% \begin{figure}[htb]
%   \caption{\label{fig_circulo}A delimitação do espaço}
%   \begin{center}
%   \includegraphics[scale=0.75]{myfig.pdf}
%   \end{center}
%   \legend{Fonte: os autores}
%   \end{figure}




% \newcommand{\subfiguras} {
%   \begin{figure}[htb]
%   \centering
%   \caption{Figuras apresentadas com o pacote \textit{subfigure}.}
%   \vspace*{-0.2cm}
%    \subfigure[\usardescricaoimagem] {\label{subfig:\referenciar}
   
%  \includegraphics[width=0.4\textwidth]{\usarnomefigura} 
%  }  \ \ \ \ \ \ \
%  \subfigure[\usardescricaoimagem] {\label{subfig:\referenciar}
%  \includegraphics[width=0.4\textwidth]{\usarnomefiguradois}
%  }
%   \vspace*{-0.3cm}
%   \legend{Fonte: \usarlegendaimagem}
%   \end{figure}
 



% \begin{figure}[h]
%   \centering
%   \subfigure[Leão]{ \label{subfig:leao}
%   \includegraphics[width=0.4\textwidth]{\usarnomefigura}
%   } \ \ \ \ \ \ \
%   \subfigure[Gráfico]{ \label{subfig:grafico}
%   \includegraphics[width=0.4\textwidth]{\usarnomefiguradois}
%   }
%   \caption{Figuras apresentadas com o pacote \textit{subfigure}.}
%   \label{fig:leao_grafico}
%   \end{figure}


%  }






% \begin{figure}[h]
%   \centering
%   \subfigure[Leão]{ \label{subfig:leao}
%   \includegraphics[width=0.4\textwidth]{lion_large.png}
%   } \ \ \ \ \ \ \
%   \subfigure[Gráfico]{ \label{subfig:grafico}
%   \includegraphics[width=0.4\textwidth]{inferential-statistics.jpg}
%   }
%   \caption{Figuras apresentadas com o pacote \textit{subfigure}.}
%   \label{fig:leao_grafico}
%   \end{figure}




%%%%%%%%%%%%%%%%%%%%%%Edicao texto 

\newcommand{\negrito}[1]{\textbf{#1}} 
\newcommand{\italico}[1]{\textit{#1}}
\newcommand{\fracao}[2]{\frac{#1}{#2}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%% Página%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\novapagina}{\newpage} 
\newcommand{\incluir}[1]{\include{#1}} 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%comando para link%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \providecommand{\linkum}{} % comando para endereco url
 \newcommand{\site}[1]{\renewcommand{\linkum}{#1}}
 \providecommand{\linkdois}{} % comando para  nome a ser colocado para referenciar o endereco
\newcommand{\nomesite}[1]{\renewcommand{\linkdois}{#1}}
\newcommand{\linkar}{\href{\linkum}{\linkdois}} %comando para inserir endereco url

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%% Elementos textuais%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\newcommand{\capitulo}{\chapter}%traduzindo capitulo
\newcommand{\capitulo}[1]{\chapter{\textbf{#1}}}%traduzindo capitulo
\newcommand{\secao}[1]{\section{\textsc{#1}}}%traduzindo secao
\newcommand{\justificativa}{\chapter{\textsc{\negrito{Justificativa}}}}%traduzindo justificativa
\newcommand{\introducao}{\chapter{\textsc{\textbf{Introdução}}}}
\newcommand{\conclusao}{\chapter{Conclusão}} %traduzindo conclusao
\newcommand{\objgeral}{\chapter{Objetivo Geral}}%traduzindo objetivo geral
\newcommand{\objespecifico}{\chapter{Objetivo Específico}}%traduzindo objetivo especifico
\newcommand{\subsecao}[1]{\subsection{\textsc{#1}}}%traduzindo subsecao
\newcommand{\subsubsecao}[1]{\negrito{\subsubsection{#1}}}%traduzindo subsubsecao
\newcommand{\metodologia}{\chapter{\textsc{Metodologia}}}%traduzindo metodologia
\newcommand{\desenvolvimento}{\chapter{\textsc{Desenvolvimento}}}%traduzindo desenvolvimento
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %%%%%%%%%%%%%%%%%%%%%%% Notas de rodapé%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \newcommand{\rodape}{\footnote} %traduzindo rodape
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



 %%%%%%%%%%%%%%%%%%%%% comando para usarlogo%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\providecommand{\usarlogo}{} %comando para usar a logo
\newcommand{\logo}[1] {\renewcommand{\usarlogo}{#1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




%%%%%%%%%%%%%%%Citacao curta &%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \providecommand{\citacaocurta}{} % comando para citacao curta
\newcommand{\citacaocurta}[1]{" #1 "}
% {\renewcommand{\citacaocurta}{“#1"}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%% Citacao longa %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% \newcommand{\iniciocitacao}{\begin{citacao}
%   \newcommand{\finalcitacao}{\end{citacao}
\newcommand{\citacaolonga}[1]{\begin{citacao} #1 \end{citacao}}




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Comandos auxiliares %%%%%%%%%%%%%%%%%%%%%%%%%%%%

\providecommand{\nomecurso}{} % comando para endereco url
 \newcommand{\curso}[1]{\renewcommand{\nomecurso}{#1}}
\newcommand{\imprimircurso}{\nomecurso} 


\providecommand{\aprovacao}{} % comando para endereco url
 \newcommand{\aprovadoem}[1]{\renewcommand{\aprovacao}{#1}}
\newcommand{\imprimiraprovacao}{\aprovacao} 




\providecommand{\bancaum}{} % comando para endereco url
 \newcommand{\nomebancaum}[1]{\renewcommand{\bancaum}{#1}}

 \providecommand{\tituloum}{} % comando para endereco url
 \newcommand{\titulobancaum}[1]{\renewcommand{\tituloum}{#1}}

 \providecommand{\instituicaoum}{} % comando para endereco url
 \newcommand{\bancauminstituicao}[1]{\renewcommand{\instituicaoum}{#1}}


\newcommand{\imprimirbancaum}{\assinatura{\textbf{\bancaum} \\ \tituloum \\ \instituicaoum}} 




\providecommand{\bancadois}{} % comando para endereco url
 \newcommand{\nomebancadois}[1]{\renewcommand{\bancadois}{#1}}

 \providecommand{\titulodois}{} % comando para endereco url
 \newcommand{\titulobancadois}[1]{\renewcommand{\titulodois}{#1}}

 \providecommand{\instituicaodois}{} % comando para endereco url
 \newcommand{\bancadoisinstituicao}[1]{\renewcommand{\instituicaodois}{#1}}


\newcommand{\imprimirbancadois}{\assinatura{\textbf{\bancadois} \\ \titulodois \\ \instituicaodois}} 




\providecommand{\bancatres}{} % comando para endereco url
 \newcommand{\nomebancatres}[1]{\renewcommand{\bancatres}{#1}}

 \providecommand{\titulotres}{} % comando para endereco url
 \newcommand{\titulobancatres}[1]{\renewcommand{\titulotres}{#1}}

 \providecommand{\instituicaotres}{} % comando para endereco url
 \newcommand{\bancatresinstituicao}[1]{\renewcommand{\instituicaotres}{#1}}


\newcommand{\imprimirbancatres}{\assinatura{\textbf{\bancatres} \\ \titulotres \\ \instituicaotres}} 



\newcommand{\apontarImagem}[1]{\autoref{#1}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%% comando capa  do ifba%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\capaifba}{  %capa com logo que foi atribuido no comando na foto
%%
\newpage
\begin{center} %centralliza
\negrito{\textsc{\imprimirinstituicao}} %inclue a instituição

\negrito{\textsc{\imprimircurso}}
\end{center} 
\begin{center}
\thispagestyle{empty} %tirannumero
\vspace*{\fill}
\negrito{\textsc{\imprimirautor}}
\end{center}
\vspace*{\fill}
\begin{center}
\textbf{\textsc{\imprimirtitulo}}
\end{center}
\vspace*{\fill}
\begin{center}
%
\negrito{\imprimirlocal} 
\vspace*{-0.4cm}

\negrito{\imprimirdata}
\end{center}
\newpage
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%MODIFICANDO A FOLHA DE ROSTO %%%%%%%%%%%%%%%%%%%%%%%%%%%

\makeatletter
\newcommand{\folhaderostoifba}{
\begin{center}
{\ABNTEXchapterfont \imprimirautor}

\vspace*{\fill}\vspace*{\fill}

{\ABNTEXchapterfont\bfseries\imprimirtitulo}

\vspace*{\fill}
\abntex@ifnotempty{\imprimirpreambulo}{%
\hspace{.45\textwidth}
\begin{minipage}{.5\textwidth}
  \SingleSpacing
  \imprimirpreambulo
\end{minipage}%
\vspace*{\fill}
}%

\vspace*{\fill}
{\negrito{\imprimirlocal}}
\vspace*{-0.4cm}

{\negrito{\imprimirdata}}
\vspace*{1cm}
\end{center}
}
\makeatother
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%% FOLHA DE APROVAÇÃO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\newcommand{\folhadeaprovacaoifba}{
  \newpage
  \begin{center}
    {\ABNTEXchapterfont\imprimirautor}

    \vspace*{\fill}\vspace*{\fill}
    \begin{center}
      \ABNTEXchapterfont\bfseries\imprimirtitulo
    \end{center}
    \vspace*{\fill}
    
    \hspace{.45\textwidth}
    \begin{minipage}{.5\textwidth}
        \imprimirpreambulo
    \end{minipage}%
    \vspace*{\fill}
   \end{center}
        
   Aprovado em: \imprimiraprovacao
\begin{center}
\negrito{BANCA EXAMINADORA}
\end{center}

  \imprimirbancaum 
  \imprimirbancadois
  \imprimirbancatres


}

% ---


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




%%%%%%%%%%%%%%%% referências %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\providecommand{\nomebibliografia}{} % cria comando para configurar para  o nome da bibliografia
\newcommand{\referencias}[1] {\renewcommand{\nomebibliografia}{#1}}
\providecommand{\arquivobibliografico}{}  % cria comando para endereçår a bibliografia
\newcommand{\arquivo}[1]{\renewcommand{\arquivobibliografico}{#1}}
\newcommand{\bibliografia}{    %usa os comandos criados e configura a bibliografia
\renewcommand{\bibname}{\nomebibliografia}
\bibliography{\arquivobibliografico}}
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%% comandos para gerenciar as informaçoes do pdf%%%%%%%%%%%%%%%%%%%%
 \providecommand{\usarassunto}{} %criando comando para inserir assundo nas informacoes pdf
 \newcommand{\assunto}[1] {\renewcommand{\usarassunto}{#1}}
 \providecommand{\chaveum}{} %criando comando para inserir primeira nas informacoes pdf
 \newcommand{\palavrachaveum}[1] {\renewcommand{\chaveum}{#1}}
 \providecommand{\chavedois}{} %criando comando para inserir segunda nas informacoes pdf
 \newcommand{\palavrachavedois}[1] {\renewcommand{\chavedois}{#1}}
 \providecommand{\chavetres}{} %criando comando para inserir terceira nas informacoes pdf
  \newcommand{\palavrachavetres}[1] {\renewcommand{\chavetres}{#1}}
 \providecommand{\chavequatro}{} %criando comando para inserir terceira nas informacoes pdf
 \newcommand{\palavrachavequatro}[1] {\renewcommand{\chavequatro}{#1}}
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


 %%%%%%%%%%%%%%%%%%%%%%%%% informacoes do pdf %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \newcommand{\informacoespdf}	{ %imprime informações do PDF na caixa propriedades deve ser inserido antes do begin document
  \hypersetup{
 pdftitle={\imprimirtitulo}, %informa o titulo
 pdfauthor={\imprimirautor},%informa o autor
pdfsubject={\usarassunto},%informa o assunto
 pdfkeywords={\chaveum}{\chavedois}{\chavetres}{\chavequatro}, %informa as palavras chave
 pdfproducer={LaTeX with abnTeX2}, % producer of the document
  pdfcreator={Adobe Reader},
 colorlinks=true,%cor do link verdadeiro ou false
  linkcolor=black,% cor do link
   citecolor=black,%cor da citacao de cor
   urlcolor=black%cor do enderço url
  }
  }





\newcommand{\imprimirdedicatoria}[1]{

\newpage
  
\begin{dedicatoria}
    
    \vspace*{\fill}
    
    \centering
    
    \noindent
    
    \textit{#1} \vspace*{\fill}

 \end{dedicatoria}

} 


%%%%%%%%%%%%%%%%%%%%%%%REGRAS DE CITAÇÃO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% cITACAO NO FINAL DO TEXTO,  INDIRETA, entre parênteses, caixa alta, ano (PINTO e MATOS, 2016) 

% cITACAO NO FINAL DO TEXTO,  DIRETA, entre parênteses, caixa alta, ano e página  (TELES, 2004, p. 3)

% Citacao indireta  no ínicio do texto, Escreve normal com o ano entre parênteses Prado e Alioto (2011)


% Citacao direta no ínicio do texto, escreve normal com ano, página entre parênteses

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%% Referência bibliografica %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Alinhamento à esquerda

% Último sobrenome em caixa alta, se tiver mais de um autor fica com ponto e vírgula.  Título em negrito 



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%% Citacoes %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\indiretaInicio}[1]{\citeonline{#1}}

\newcommand{\indiretaFinal}[1]{\cite{#1}}


\newcommand{\diretaInicio}[2]{\citeonline[p.#1]{#2}}
\newcommand{\diretaFinal}[2]{\cite[p.#1]{#2}}



    

         """
    
    with open(arquivo+"/ptex.sty","a") as pacote:
            pacote.write(ifba)
    pacote.close
    
    arquivo_tex=r"""
    
    %%%%%%  CABECALHO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



\documentclass[
% -- opções da classe memoir --
12 pt,				% tamanho da fonte
openright,			% capítulos começam em pág ímpar (insere página vazia caso preciso)
%twoside,			% para impressão em verso e anverso. Oposto a oneside
oneside,
a4paper,			% tamanho do papel. 
% -- opções da classe abntex2 --
chapter=TITLE,		% títulos de capítulos convertidos em letras maiúsculas
%	section=TITLE,		% títulos de seções convertidos em letras maiúsculas
%	subsection=TITLE,	% títulos de subseções convertidos em letras maiúsculas
%	subsubsection=TITLE,% títulos de subsubseções convertidos em letras maiúsculas
% -- opções do pacote babel --
english,			% idioma adicional para hifenização
brazil	               % o último idioma é o principal do documento
]{abntex2}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\usepackage{ptex}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CONFIGURAÇÃO DOS DADOS  DO TRABALHO
     """
    t1=r"\titulo{"
    t2="{}".format(titulo)
    t3=r"}"
    Titulo=t1+t2+t3+"\n"

# \titulo{titulo} % ESCOLHER APENAS UM TERMO E EXPLICAR NO TEXTO O RESTANTE
  ############ modificar ################  
    a1=r"\autor{"
    a2="{}".format(autor)
    a3=r"}"
    Autor=a1+a2+a3+"\n"
# \autor{EVERTON DE JESUS SANTOS}
    l1=r"\local{"
    l2="{}".format(local)
    l3=r"}"
    Local=l1+l2+l3+"\n"
# \local{Santo Amaro}
    d1=r"\data{"
    d2="{}".format(data)
    d3=r"}"
    Data=d1+d2+d3+"\n"
# \data{2022}
    o1=r"\orientador{"
    o2="{}".format(orientador)
    o3=r"}"
    Orientador=o1+o2+o3+"\n"
# \orientador{xxxxxxx}

    da1=r"\aprovadoem{"
    da2="{}".format(dataparovacao)
    da3=r"}"
    Dataaprovacao=da1+da2+da3+"\n"
# \aprovadoem{28 de janeiro de 2022.}

    i1=r"\instituicao{"
    i2="{}".format(instituicao)
    i3=r"}"
    Instituicao=i1+i2+i3+"\n"
# \instituicao{INSTITUTO FEDERAL DE CIENCIA E TECNOLOGIA DA BAHIA}
    c1=r"\curso{"
    c2="{}".format(curso)
    c3=r"}"
    Curso=c1+c2+c3+"\n"
# \curso{LICENCIATURA  EM COMPUTAÇÃO}

    arquivo_tex_dois=r"""
\palavrachaveum{Palavra chave1 }
\palavrachavedois{Palavra chave2 }
\palavrachavetres{Palavra chave3 }
\tipotrabalho{Monografia}


\nomebancaum{TEste}
\titulobancaum{Mestre em Educação}
\bancauminstituicao{Instituto Federal de Ciência e e e ee}


\nomebancadois{TEste}
\titulobancadois{Mestre em Educação}
\bancadoisinstituicao{Instituto Federal de Ciência e e e ee}


\nomebancatres{TEste}
\titulobancatres{Mestre em Educação}
\bancatresinstituicao{Instituto Federal de Ciência e e e ee}



% O preambulo deve conter o tipo do trabalho, o objetivo, 
% o nome da instituição e a área de concentração 

\preambulo{Trabalho apresentado como requisito parcial para obtenção do título de
Licenciado em Computação  pelo Instituto Federal de Educação Ciência e Tecnologia da Bahia, \italico{campus} Santo Amaro, sob
orientação da Profa. \imprimirorientador . }

% Espaçamentos entre linhas e parágrafos 
% O tamanho do parágrafo é dado por:
\setlength{\parindent}{1.5cm}

% Controle do espaçamento entre um parágrafo e outro:
\setlength{\parskip}{0.2cm}  % tente também \onelineskip


%%%%%%%%%%% INDICE REMISSIVO

\informacoespdf

%%%%%%%%%%%% Início do Documento
\inicio


\pretextual
\capaifba

\folhaderostoifba

\folhadeaprovacaoifba


\imprimirdedicatoria{ a testes de ddfsfsdf dsf sdflksdfçksdmf  dkfjsdçfj kjsdf  sfçj }

\listoffigures*
\sumario
\textual





\arquivo{bibliografia}

\referencias{REFERÊNCIAS}

\bibliografia



\fim



""" 
    
    
    with open(arquivo+"/arquivo.tex","a") as arquivo:
        arquivo.write(arquivo_tex)
        arquivo.write(Titulo)
        arquivo.write(Autor)
        arquivo.write(Local)
        arquivo.write(Data)
        arquivo.write(Orientador)
        arquivo.write(Dataaprovacao)
        arquivo.write(Instituicao)
        arquivo.write(Curso)
        arquivo.write(arquivo_tex_dois)
    arquivo.close
     
     
    




#####################################################################################################

def citacoes():
       #título da janela
    
    newWindow = Toplevel()
    newWindow.title("Citacoes")
    newWindow.geometry("270x125")
    newWindow.config(bg="gray")
    newWindow.resizable(False,False)

   

    Label(newWindow,text ="Nome do comando").grid(row=1,column=1, sticky="NESW")



    nomeComando=tk.Entry(newWindow)
    nomeComando.grid(row=1,column=2, sticky="NESW")


    Label(newWindow,text ="Citacao").grid(row=2,column=1, sticky="NESW")



    citacao=tk.Entry(newWindow)
    citacao.grid(row=2,column=2, sticky="NESW")
    
    
    
    Label(newWindow,text ="Descrição da Citação").grid(row=3,column=1, sticky="NESW")



    descricao=tk.Entry(newWindow)
    descricao.grid(row=3,column=2, sticky="NESW")


    Label(newWindow,text ="Autor").grid(row=4,column=1, sticky="NESW")



    autorCitacao=tk.Entry(newWindow)
    autorCitacao.grid(row=4,column=2, sticky="NESW")

    Label(newWindow,text ="Titulo obra").grid(row=5,column=1, sticky="NESW")



    tituloObra=tk.Entry(newWindow)
    tituloObra.grid(row=5,column=2, sticky="NESW")
    
    def gerar():
        tx_titulo=tituloObra.get()
        tx_autor=autorCitacao.get()
        tx_citacao=citacao.get()
        tx_descricao=descricao.get()
        tx_comando=nomeComando.get()
      

        gerar_citacoes(tx_titulo,tx_autor,tx_citacao,tx_descricao,tx_comando)
        

    Button(newWindow,text="Gerar",command=gerar).grid(row=9,columnspan=3,sticky="NESW")


   

########################################################################################################    
def gerar_citacoes(tx_titulo,tx_autor,tx_citacao,tx_descricao,tx_comando):
  
  arquivo = tkinter.filedialog.askdirectory(title="Selecione o local onde está o arquivo de citações")
  
  c1=r"\providecommand{\usarcitacao"+tx_comando
  c2=r"}{}"+"\n"
  c3=r"\newcommand{"
  c4=f"\{tx_comando}"
  c40=r"}"
  c41=r"[1]{\renewcommand{"
  c5=r"\usarcitacao"
  c51=tx_comando
  c6=r"}{#1}}"+"\n"
  c7=f"\{tx_comando}"
  c8=r"{"
  c9=tx_citacao
  c10="}\n"
  comando=c1+c2+c3+c4+c40+c41+c5+c51+c6+c7+c8+c9+c10



  with open(arquivo+"/citacao.sty","a") as citacao:
        citacao.write(comando)
  citacao.close
  


  ###########################################################################################################

def bibliografia():
       #título da janela
    
    newWindow = Toplevel()
    newWindow.title("Bibliografia")
    newWindow.geometry("270x180")
    newWindow.config(bg="gray")
    newWindow.resizable(False,False)

   

    Label(newWindow,text ="Tipo").grid(row=1,column=1, sticky="NESW")


    tipoBibliografia = ttk.Combobox(newWindow, 
                            values=[
                                    "Eletrônico", 
                                    "Livro",
                                    "Artigo",
                                    "Monografia",
                                    "Manual",
                                    "Tese Doutorado",
                                    "Dissertação Mestrado"])
 
    tipoBibliografia.grid(row=1,column=2, sticky="NESW")

    Label(newWindow,text ="Nome da Referência").grid(row=2,column=1, sticky="NESW")
    nomeReferencia=tk.Entry(newWindow)
    nomeReferencia.grid(row=2,column=2, sticky="NESW")
    Label(newWindow,text ="Autor").grid(row=3,column=1, sticky="NESW")
    autor=tk.Entry(newWindow)
    autor.grid(row=3,column=2, sticky="NESW")
    Label(newWindow,text ="Título").grid(row=4,column=1, sticky="NESW")
    titulo=tk.Entry(newWindow)
    titulo.grid(row=4,column=2, sticky="NESW")
    Label(newWindow,text ="Endereço Eletrônico").grid(row=5,column=1, sticky="NESW")
    endereco=tk.Entry(newWindow)
    endereco.grid(row=5,column=2, sticky="NESW")
    Label(newWindow,text ="Ano").grid(row=6,column=1, sticky="NESW")
    ano=tk.Entry(newWindow)
    ano.grid(row=6,column=2, sticky="NESW")
    Label(newWindow,text ="Acesso em:").grid(row=7,column=1, sticky="NESW")
    dataAcesso=tk.Entry(newWindow)
    dataAcesso.grid(row=7,column=2, sticky="NESW")
    Label(newWindow,text ="Escola:").grid(row=8,column=1, sticky="NESW")
    escola=tk.Entry(newWindow)
    escola.grid(row=8,column=2, sticky="NESW")
    # https://jufajardini.wordpress.com/2013/10/09/latex-adicionar-data-de-acesso-a-referencias-abntex2/
    # urlaccessdate
    def gerar():
      arquivo = tkinter.filedialog.askdirectory(title="Selecione o local onde está o arquivo de Referências")
      if tipoBibliografia.get()== "Eletrônico" or tipoBibliografia.get()== "Artigo":
        r1=r"@Electronic{"
        r2=nomeReferencia.get()
        r3=",\n"
        r30=r"title={"
        r31=titulo.get()
        r32=r"},"
        r33="\n"
        r4=r"author={"
        r5=autor.get()
        r6=r"}"
        r60=",\n"
        r7=r"url={"
        r8=endereco.get()
        r9="},\n "
        r10=r"year={"
        r11=ano.get()
        r12="},\n "
        r13=r"urlaccessdate={"
        r14=dataAcesso.get()
        r15="},\n}\n\n"
        referencia=r1+r2+r3+r30+r31+r32+r33+r4+r5+r6+r60+r7+r8+r9+r10+r11+r12+r13+r14+r15
        with open(arquivo+"/bibliografia.bib","a") as  bibliografia:
          bibliografia.write(referencia)
        bibliografia.close

      if tipoBibliografia.get()== "Livro":
        r1=r"@Book{"
        r2=nomeReferencia.get()
        r3=",\n"
        r30=r"title={"
        r31=titulo.get()
        r32=r"},"
        r33="\n"
        r4=r"author={"
        r5=autor.get()
        r6=r"}"
        r60=",\n"
        r7=r"url={"
        r8=endereco.get()
        r9="},\n "
        r10=r"year={"
        r11=ano.get()
        r12="},\n "
        r13=r"urlaccessdate={"
        r14=dataAcesso.get()
        r15="},\n}\n\n"
        referencia=r1+r2+r3+r30+r31+r32+r33+r4+r5+r6+r60+r7+r8+r9+r10+r11+r12+r13+r14+r15
        with open(arquivo+"/bibliografia.bib","a") as  bibliografia:
          bibliografia.write(referencia)
        bibliografia.close

      if tipoBibliografia.get()== "Monografia":
          r1=r"@Thesis{"
          r2=nomeReferencia.get()
          r3=",\n"
          r30=r"title={"
          r31=titulo.get()
          r32=r"},"
          r33="\n"
          r4=r"author={"
          r5=autor.get()
          r6=r"},"
          r60=r",\n"
          a=r"type={"
          b="Monografia"
          c=r"},"
          r60="\n"
          r61=r"institution= {"
          r62=escola.get()
          r63="},\n"
          r7=r"url={"
          r8=endereco.get()
          r9="},\n "
          r10=r"year={"
          r11=ano.get()
          r12="},\n "
          r13=r"urlaccessdate={"
          r14=dataAcesso.get()
          r15="},\n}\n\n"
          referencia=r1+r2+r3+r30+r31+r32+r33+r4+r5+r6+r60+a+b+c+r61+r62+r63+r7+r8+r9+r10+r11+r12+r13+r14+r15
          with open(arquivo+"/bibliografia.bib","a") as  bibliografia:
            bibliografia.write(referencia)
          bibliografia.close
    
      if tipoBibliografia.get()== "Manual":
          r1=r"@Manual{"
          r2=nomeReferencia.get()
          r3=",\n"
          r30=r"title={"
          r31=titulo.get()
          r32=r"},"
          r33="\n"
          r4=r"author={"
          r5=autor.get()
          r6=r"}"
          r60=",\n"
          r7=r"url={"
          r8=endereco.get()
          r9="},\n "
          r10=r"year={"
          r11=ano.get()
          r12="},\n "
          r13=r"urlaccessdate={"
          r14=dataAcesso.get()
          r15="},\n}\n\n"
          referencia=r1+r2+r3+r30+r31+r32+r33+r4+r5+r6+r60+r7+r8+r9+r10+r11+r12+r13+r14+r15
          with open(arquivo+"/bibliografia.bib","a") as  bibliografia:
            bibliografia.write(referencia)
          bibliografia.close
        
      if tipoBibliografia.get()== "Tese Doutorado":
        r1=r"@phdthesis{"
        r2=nomeReferencia.get()
        r3=",\n"
        r30=r"title={"
        r31=titulo.get()
        r32=r"},"
        r33="\n"
        r4=r"author={"
        r5=autor.get()
        r6=r"}"
        r60=",\n"
        r61=r"School= {"
        r62=escola.get()
        r63="},\n"
        r7=r"url={"
        r8=endereco.get()
        r9="},\n "
        r10=r"year={"
        r11=ano.get()
        r12="},\n "
        r13=r"urlaccessdate={"
        r14=dataAcesso.get()
        r15="},\n}\n\n"
        referencia=r1+r2+r3+r30+r31+r32+r33+r4+r5+r6+r60+r61+r62+r63+r7+r8+r9+r10+r11+r12+r13+r14+r15
        with open(arquivo+"/bibliografia.bib","a") as  bibliografia:
          bibliografia.write(referencia)
        bibliografia.close
      
      
      if tipoBibliografia.get()== "Dissertação Mestrado":
        r1=r"@MastersThesis{"
        r2=nomeReferencia.get()
        r3=",\n"
        r30=r"title={"
        r31=titulo.get()
        r32=r"},"
        r33="\n"
        r4=r"author={"
        r5=autor.get()
        r6=r"}"
        r60=",\n"
        r61=r"School= {"
        r62=escola.get()
        r63="},\n"
        r7=r"url={"
        r8=endereco.get()
        r9="},\n "
        r10=r"year={"
        r11=ano.get()
        r12="},\n "
        r13=r"urlaccessdate={"
        r14=dataAcesso.get()
        r15="},\n}\n\n"
        referencia=r1+r2+r3+r30+r31+r32+r33+r4+r5+r6+r60+r61+r62+r63+r7+r8+r9+r10+r11+r12+r13+r14+r15
        with open(arquivo+"/bibliografia.bib","a") as  bibliografia:
          bibliografia.write(referencia)
        bibliografia.close
    


    Button(newWindow,text="Gerar",command=gerar).grid(row=9,columnspan=3,sticky="NESW")






########################################################################################################################################
def mostrar_sobre():
    messagebox.showinfo("Sobre PTeX","2022\n\nVERSÂO 1.0!\n\nTradução LateX\nEverton Santos\nevertonsantos@tinoober.com")

    
   

####################################################################################################################################



#instanciando a janela principal
janela=tk.Tk()



#icone da janela
#logo da aplicação
janela.tk.call("wm","iconphoto",janela._w,tk.PhotoImage(file="logo.png"))

#título da janela
janela.title("PTeX  ver 1.0")
janela.geometry("225x150")
janela.config(bg="white")
janela.resizable(False,False)





# Barra de menu
barra_menu=tk.Menu()


#menu arquivo
menu_arquivo=tk.Menu(tearoff=0)
menu_arquivo.add_command(label="Sair",command=janela.quit)
barra_menu.add_cascade(label="Arquivo",menu=menu_arquivo)


#menu ajuda
menu_ajuda=tk.Menu(tearoff=0)

menu_ajuda.add_command(label="Manual",command= mostrar_manual)
menu_ajuda.add_command(label="Sobre",command= mostrar_sobre)
barra_menu.add_cascade(label="Ajuda",menu=menu_ajuda)
janela.config(menu=barra_menu)






#titulo dentro da janela com grid
titulo=tk.Label(text="Escolha uma das opções abaixo:",bg="white",height=2)
titulo.grid(row=0,columnspan=3, sticky="NESW")

#botao com imagem esquerda gerar template
# botao=tk.Button(command=gerar_template)
botao=tk.Button(command=formulario)
img_button=tk.PhotoImage(file="botaocriar.png")
botao.config(image=img_button,bg="white",bd=0,highlightthickness=0,highlightbackground=None,activebackground="white")
botao.grid(row=1,column=0)
#label com grid esquerda
msg=tk.Label(text="Criar",bg="white")
msg.grid(row=3,column=0)



#botao com imagem centro Criar citacoes
botao2=tk.Button(command=citacoes)
img_button2=tk.PhotoImage(file="botaocitacao.png")
botao2.config(image=img_button2,bg="white",bd=0,highlightthickness=0,highlightbackground=None,activebackground="white")
botao2.grid(row=1,column=1)
#label com grid esquerda
msg=tk.Label(text="Citação",bg="white")
msg.grid(row=3,column=1)


#botao com imagem direita Bibliografia
botao3=tk.Button(command=bibliografia)
img_button3=tk.PhotoImage(file="botaobibliografia.png")
botao3.config(image=img_button3,bg="white",bd=0,highlightthickness=0,highlightbackground=None,activebackground="white")
botao3.grid(row=1,column=2)
#label com grid esquerda
msg=tk.Label(text="Referências",bg="white")
msg.grid(row=3,column=2)



janela.mainloop()




