[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL3 License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Ask Me Anything][ask-me-anything]][personal-page]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/stiliajohny/python-git-pusher">
    <img src="https://raw.githubusercontent.com/stiliajohny/python-git-pusher/master/.assets/logo.png" alt="Main Logo" width="80" height="80">
  </a>

  <h3 align="center">python-git-pusher</h3>

  <p align="center">
    Push files to multiple repos in one go
    <br />
    <a href="https://github.com/stiliajohny/python-git-pusher/blob/master/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/stiliajohny/python-git-pusher/issues/new?labels=i%3A+bug&template=1-bug-report.md">Report Bug</a>
    ·
    <a href="https://github.com/stiliajohny/python-git-pusher/issues/new?labels=i%3A+enhancement&template=2-feature-request.md">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Example Config](#example-config)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project

This project is created out of neccessity to push multiple files into multiple git repos at once.
For example push a LICENSE or ISSUE TEMPLATE or Update a Github Action. This project is not limited to this.

### Built With

- Python
- GIT
- Poetry

---

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Install Python 3.6 or higher

### Installation

- Install the tool via `pip3 install git-pusher`

---

<!-- USAGE EXAMPLES -->

## Usage

- Create a config yaml with all the repos and the files ( relative or absulute paths )
- Run the command `git-pusher --config ./config.yaml --branch branch-name`

### Example Config

```yaml
repos:
  - git@github.com:stiliajohny/test1.git
  - git@github.com:stiliajohny/test2.git
  - git@github.com:stiliajohny/test3.git

files:
  - ./LICENSE.md
  - ./README.md
  - ./CHANGELOG.md
  - ./CONTRIBUTING.md
  - ./CODE_OF_CONDUCT.md
  - ./CONFIG.md
```

---

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/stiliajohny/python-git-pusher/issues) for a list of proposed features (and known issues).

---

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<!-- LICENSE -->

## License

Distributed under the GPLv3 License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

John Stilia - stilia.johny@gmail.com

<!--
Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)
-->

---

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/stiliajohny/python-git-pusher.svg?style=for-the-badge
[contributors-url]: https://github.com/stiliajohny/python-git-pusher/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/stiliajohny/python-git-pusher.svg?style=for-the-badge
[forks-url]: https://github.com/stiliajohny/python-git-pusher/network/members
[stars-shield]: https://img.shields.io/github/stars/stiliajohny/python-git-pusher.svg?style=for-the-badge
[stars-url]: https://github.com/stiliajohny/python-git-pusher/stargazers
[issues-shield]: https://img.shields.io/github/issues/stiliajohny/python-git-pusher.svg?style=for-the-badge
[issues-url]: https://github.com/stiliajohny/python-git-pusher/issues
[license-shield]: https://img.shields.io/github/license/stiliajohny/python-git-pusher?style=for-the-badge
[license-url]: https://github.com/stiliajohny/python-git-pusher/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/johnstilia/
[product-screenshot]: .assets/screenshot.png
[ask-me-anything]: https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg?style=for-the-badge
[personal-page]: https://github.com/stiliajohny
