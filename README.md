# Sistema de Agendamento de Consultas Médicas 🏥

Projeto desenvolvido em **Python** com **Flask** para gerenciar agendamentos de consultas médicas de forma simples e intuitiva.  
Permite cadastrar pacientes, escolher especialidade, data e horário da consulta, com validação de CPF e telefone.

---


---

## ⚙ Funcionalidades

- Cadastro de pacientes com:
  - Nome completo
  - Especialidade médica (Cardiologia, Dermatologia, Pediatria, Geriatria, Alergista)
  - Telefone com DDD
  - CPF
  - Data e horário da consulta
- Validação de CPF e telefone para garantir apenas números corretos
- Carregamento dinâmico de horários disponíveis conforme a data escolhida
- Exibição de confirmação de agendamento
- Layout responsivo usando **Bootstrap 5** e CSS personalizado
- Projeto modular com separação de templates e arquivos estáticos

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **Flask** (microframework web)
- **Jinja2** (templates do Flask)
- **HTML5 / CSS3**
- **Bootstrap 5** (estilização responsiva)
- Ambiente virtual Python (`venv`) recomendado

---

## 🚀 Instalação e Execução

1. Clone este repositório:
```bash
git clone https://github.com/mariaeduardaolvr/Sistemas-de-agendamentos.git
