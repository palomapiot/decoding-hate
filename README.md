# Decoding Hate

## Overview
**Decoding Hate** is a project aimed at analyzing and understanding LLMs reactions to hate speech. The repository contains the input datasets, models, prompts, and LLMs' generated responses related to the project.

## Contents
- `data/` - Directory containing datasets used for the analysis.
- `models/` - Directory containing the hate speech classification model and the finetuned models.
- `prompts/` - Directory with the prompts used to reduce hate speech generation on LLMs.
- `responses/` - Directory with the generated responses.

## Citation

If you use **CONAN dataset**, please cite:

```bibtex
@inproceedings{bonaldi-etal-2022-human,
    title = "Human-Machine Collaboration Approaches to Build a Dialogue Dataset for Hate Speech Countering",
    author = "Bonaldi, Helena  and
      Dellantonio, Sara  and
      Tekiroglu, Serra Sinem and
      Guerini, Marco",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    publisher = "Association for Computational Linguistics",
    url = "https://preview.aclanthology.org/emnlp-22-ingestion/2022.emnlp-main.549/",
    pages = "8031--8049",
}

@inproceedings{fanton-2021-human,
    title="{Human-in-the-Loop for Data Collection: a Multi-Target Counter Narrative Dataset to Fight Online Hate Speech}",
    author="{Fanton, Margherita and Bonaldi, Helena and Tekiroğlu, Serra Sinem and Guerini, Marco}",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics",
    month = aug,
    year = "2021",
    publisher = "Association for Computational Linguistics",
}

@inproceedings{chung-etal-2019-conan,
    title = "{CONAN} - {CO}unter {NA}rratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech",
    author = "Chung, Yi-Ling and Kuzmenko, Elizaveta and Tekiroglu, Serra Sinem and Guerini, Marco",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P19-1271",
    doi = "10.18653/v1/P19-1271",
    pages = "2819--2829"
}

@inproceedings{chung-etal-2021-knowledge,
    title = "{Towards Knowledge-Grounded Counter Narrative Generation for Hate Speech",
    author = "Chung, Yi-Ling and Tekiroğlu, Serra Sinem and Guerini, Marco",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
}
```

If you use **DGHS dataset**, please cite:


```bibtex
@misc{vidgen2021learning,
    title={Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection}, 
    author={Bertie Vidgen and Tristan Thrush and Zeerak Waseem and Douwe Kiela},
    year={2021},
    eprint={2012.15761},
    archivePrefix={arXiv},
    primaryClass={id='cs.CL' full_name='Computation and Language' is_active=True alt_name='cmp-lg' in_archive='cs' is_general=False description='Covers natural language processing. Roughly includes material in ACM Subject Class I.2.7. Note that work on artificial languages (programming languages, logics, formal systems) that does not explicitly address natural-language issues broadly construed (natural-language processing, computational linguistics, speech, text retrieval, etc.) is not appropriate for this area.'}
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