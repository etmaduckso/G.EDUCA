Aplicação Web de Gestão Escolar com Controle de Presença Automatizado
Visão Geral
Este projeto representa uma solução completa e robusta para a gestão escolar moderna, focada no controle de presença automatizado e na geração de relatórios detalhados. Desenvolvida com uma arquitetura de microsserviços e tecnologias de ponta, a aplicação garante escalabilidade, segurança e uma experiência de usuário intuitiva para todos os níveis de acesso: escolas, gestores, professores e alunos.

Arquitetura e Tecnologias
A aplicação foi construída seguindo uma arquitetura de microsserviços, permitindo que cada funcionalidade seja desenvolvida e escalada independentemente. A comunicação entre os microsserviços é realizada através de APIs RESTful, garantindo flexibilidade e interoperabilidade.

Back-end:
Python: Escolhido pela sua robustez, segurança e vasta biblioteca de funcionalidades para desenvolvimento web rápido e eficiente.
Banco de Dados:
PostgreSQL: Selecionado para dados relacionais, garantindo integridade e consistência.
MongoDB: Empregado para dados não relacionais, oferecendo flexibilidade e escalabilidade horizontal.
Front-end:
Flet: Escolhido para a interface de usuário, proporcionando uma experiência rica e interativa, com componentes reutilizáveis e alto desempenho.
API:
RESTful: Implementada para comunicação eficiente e padronizada entre os microsserviços e o front-end.
Destaques
Integração com Controladora de Acesso Garen: A aplicação integra-se de forma eficiente e segura com a API da controladora de acesso Garen, automatizando o registro de presença e eliminando a necessidade de processos manuais.
Segurança Robusta: A segurança dos dados é uma prioridade, com a implementação de medidas como autenticação e autorização robustas, proteção contra ataques comuns e criptografia de dados sensíveis.
Escalabilidade e Alta Disponibilidade: A arquitetura de microsserviços e a implantação em nuvem garantem que a aplicação possa lidar com um grande número de usuários e manter-se disponível em todos os momentos.
Testes Automatizados: A aplicação possui uma cobertura abrangente de testes automatizados (unitários, de integração, etc.), garantindo a qualidade e a estabilidade do código.
Documentação Completa: A API e o código são completamente documentados, com diagramas e fluxogramas, facilitando a manutenção e a evolução da aplicação.
Funcionalidades Principais
Autenticação e Autorização: Sistema de cadastro e login seguro, com controle de acesso baseado em roles (RBAC).
Gestão Escolar: Cadastro e gerenciamento de escolas, salas, turmas, disciplinas, professores e alunos.
Controle de Presença Automatizado: Integração com a controladora de acesso Garen e interface para registro manual de presença.
Relatórios Detalhados: Relatórios de presença, entrada e saída de alunos, e consolidados por escola.
Painel de Controle Intuitivo: Painel de controle personalizado para cada nível de usuário, com visualização de dados em gráficos.
Implantação
A aplicação foi projetada para ser implantada em nuvem, utilizando contêineres Docker para facilitar o gerenciamento e a escalabilidade. As instruções detalhadas para implantação estão disponíveis na documentação do projeto.

Contribuição
Contribuições são bem-vindas! Consulte o guia de contribuição para obter mais informações sobre como contribuir para este projeto.
