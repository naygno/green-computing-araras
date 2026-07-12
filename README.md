# Green Computing: Sobriedade Digital no Recanto das Araras

[![ODS 6](https://img.shields.io/badge/ODS-6%20%C3%81gua%20Pot%C3%A1vel-blue)](https://brasil.un.org/pt-br/sdgs/6)
[![ODS 7](https://img.shields.io/badge/ODS-7%20Energia%20Limpa-yellow)](https://brasil.un.org/pt-br/sdgs/7)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-success)]()

## 📌 Sobre o Projeto
Projeto de extensão universitária (UFBRA) focado na aplicação de **Lean ICT** e **Green Computing** em comunidades de baixa renda (Residencial Recanto das Araras I e II, Palmas/TO). O objetivo é mitigar o desperdício financeiro com pacotes de dados móveis e a obsolescência precoce de smartphones através do letramento digital.

A otimização de dispositivos na ponta do usuário (Edge) reduz o tráfego de rede inútil (telemetria/anúncios), impactando diretamente a eficiência energética das antenas de telecomunicação (ODS 7) e a pegada hídrica (WUE) dos Data Centers (ODS 6).

## 🏗️ Arquitetura da Solução
A intervenção é distribuída via WhatsApp em dois formatos complementares:
1. **Card de Engajamento (PNG):** Desenvolvido em Inkscape, focado em conversão rápida e configuração de DNS Privado (AdGuard).
2. **Micro-Cartilha (PDF):** Desenvolvida em LaTeX, contendo tutoriais detalhados de restrição de dados em segundo plano e desativação de autoplay.

## 📁 Estrutura do Repositório
```text
green-computing-araras/
├── .gitignore
├── LICENSE
├── README.md
├── assets/                 # Prints brutos tirados via scrcpy do celular
│   └── screenshots/
├── src/
│   ├── inkscape/           # Arquivos vetoriais (.svg) editáveis
│   └── latex/              # Código-fonte da cartilha (.tex, macros)
└── dist/                   # Arquivos finais para distribuição (PDF e PNG)
```
## 🚀 Como compilar (Build)
### LaTeX (Cartilha)
O documento utiliza a classe `article` com o tema Nord. Para compilar:
```bash
cd src/latex
pdflatex main.tex
```