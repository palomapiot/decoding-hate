# Decoding Hate

## Overview
**Decoding Hate** is a project aimed at analysing and understanding LLMs reactions to hate speech. The repository contains the input datasets, models, prompts, and LLMs' generated responses related to the project.

*Paper accepted at NAACL 2025 Main Conference*

## Contents
- `models/` - Directory containing the hate speech classification model and the finetuned models.
- `prompts/` - Directory with the prompts used to reduce hate speech generation on LLMs.
- `responses/` - Directory with the generated responses.

## Citation

If you use anything from this repository or paper, please cite:

```bibtex
@inproceedings{piot-parapar-2025-decoding,
    title = "Decoding Hate: Exploring Language Models' Reactions to Hate Speech",
    author = "Piot, Paloma  and
      Parapar, Javier",
    editor = "Chiruzzo, Luis  and
      Ritter, Alan  and
      Wang, Lu",
    booktitle = "Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",
    month = apr,
    year = "2025",
    address = "Albuquerque, New Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.naacl-long.45/",
    pages = "973--990",
    ISBN = "979-8-89176-189-6",
    abstract = "Hate speech is a harmful form of online expression, often manifesting as derogatory posts. It is a significant risk in digital environments. With the rise of Large Language Models (LLMs), there is concern about their potential to replicate hate speech patterns, given their training on vast amounts of unmoderated internet data. Understanding how LLMs respond to hate speech is crucial for their responsible deployment. However, the behaviour of LLMs towards hate speech has been limited compared. This paper investigates the reactions of seven state-of-the-art LLMs (LLaMA 2, Vicuna, LLaMA 3, Mistral, GPT-3.5, GPT-4, and Gemini Pro) to hate speech. Through qualitative analysis, we aim to reveal the spectrum of responses these models produce, highlighting their capacity to handle hate speech inputs. We also discuss strategies to mitigate hate speech generation by LLMs, particularly through fine-tuning and guideline guardrailing. Finally, we explore the models' responses to hate speech framed in politically correct language."
}
```

If you use **MetaHateBERT**, please cite:

```bibtex
@article{Piot_Martín-Rodilla_Parapar_2024,
    title={MetaHate: A Dataset for Unifying Efforts on Hate Speech Detection},
    volume={18},
    url={https://ojs.aaai.org/index.php/ICWSM/article/view/31445},
    DOI={10.1609/icwsm.v18i1.31445},
    number={1},
    journal={Proceedings of the International AAAI Conference on Web and Social Media},
    author={Piot, Paloma and Martín-Rodilla, Patricia and Parapar, Javier},
    year={2024},
    month={May},
    pages={2025-2039}
}
```

## Disclaimer

This repository includes content that may contain hate speech, offensive language, or other forms of inappropriate and objectionable material. The content present in the dataset is not created or endorsed by the authors or contributors of this project. It is collected from various sources and does not necessarily reflect the views or opinions of the project maintainers.

The purpose of using this repository is for research, analysis, or educational purposes only. The authors do not endorse or promote any harmful, discriminatory, or offensive behaviour conveyed in the dataset.

Users are advised to exercise caution and sensitivity when interacting with or interpreting the repository. If you choose to use the datasets or models, it is recommended to handle the content responsibly and in compliance with ethical guidelines and applicable laws.

The project maintainers disclaim any responsibility for the content within the repository and cannot be held liable for how it is used or interpreted by others.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

The Apache License 2.0 is an open-source license that allows you to use the software for any purpose, to distribute it, to modify it, and to distribute modified versions of the software under the terms of the license.

For more details, please refer to the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).
