import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'

export const actions: Actions = {
    create_experience: async ({ request }) => {
        const formData = await request.formData();

        const experiences = {
            title: formData.get('title'),
            description: formData.get('description'),
            startTime: formData.get('startTime'),
            endTime: formData.get('endTime'),
            link: formData.get('link'),
        }

        await fetch(`${SERVEUR_URL}/api/experiences/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(experiences),
        })

        return { success: true };
    }

}