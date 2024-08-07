class Episodes:
    @classmethod
    def get_episodes(cls, tutorial_name):
        episodes = {
            "php": [
                "First project",
                "A",
                "B",
                "C"
            ]
        }
        return episodes.get(tutorial_name)
