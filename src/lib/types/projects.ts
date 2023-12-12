import type { Skill } from "./skills"

export interface Project {
    id: number
    name: string
    description: string
    images: ProjectImage[]
    link: string
    skills: Skill[]
}

export interface ProjectImage {
    id: number
    image: string
}