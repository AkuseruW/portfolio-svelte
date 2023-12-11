import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'
import { writeFile } from 'fs/promises';


export const load: PageServerLoad = () => {
    const projects = async () => {
        return await fetch(`${SERVEUR_URL}/api/projects/`).then(res => res.json())
    }

    return {
        projects: projects()
    }
}