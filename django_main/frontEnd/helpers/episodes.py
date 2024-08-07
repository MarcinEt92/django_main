class Episodes:
    @classmethod
    def get_episodes(cls, tutorial_name):
        episodes = {
            "html": [
                "First project",
                "Website structure",
                "Links and addresses",
                "Lists",
                "New tags",
                "Forms"
            ],
            "css": [
                "First project",
                "Template styling",
                "Sticky menu",
                "Forms styling",
                "Transition, transform",
                "CSS units",
            ],
            "js": [
                "First project - timer",
                "Functions, events",
                "First game",
                "Numbers",
                "JQuery, memory game",
                "DOM hierarchy 1",
                "DOM hierarchy 2",
                "Canvas",
            ]
        }
        return episodes.get(tutorial_name)
