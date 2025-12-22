<p align="center">
  <img src="https://killshot.rip/images/KILLSHOT.svg" alt="Killshot Logo" width="500">
</p>

# Horror Movie Kill Counts

A community-driven, machine-readable database of horror movie body counts. This data powers [killshot.rip](https://killshot.rip).

## The Data

The primary data is stored in `killcounts.jsonl`. Each entry includes:

* `title`: The film's title.
* `year`: Release year.
* `count`: Total confirmed kills.
* `tmdb_id`: The Movie Database ID for easy API linking.

A `killcounts.csv` file is also available and is automatically generated from the JSONL file. Please do not edit the CSV directly.

## Credits & Sources

This project is a compilation of hard work by the horror community:

* **Dead Meat**: Many counts are sourced from James A. Janisse’s "Kill Count" series and the [Dead Meat Wiki](https://the-dead-meat.fandom.com/).
* **MovieBodyCounts**: Original data contributed by the legacy community at [moviebodycounts.com](http://www.moviebodycounts.com/).
* **Randal Olson**: For the initial 2013-2014 scraped dataset that formed the foundation of this list.

## How to Contribute

1. Fork the repo.
2. Add a new line to `killcounts.jsonl`.
3. Open a Pull Request!